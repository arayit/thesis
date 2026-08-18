#!/usr/bin/env python3
"""Exp6 (3 Aug 2026): first N2O detection since December — R15 line scan
under constant flow at 205 Torr.

Input: experimental/daq/2026-08-03/exp6-scan/ — fine scan 1297.5-1298.5
(0.1 steps, 30 s/point, TC 3 s, sens 200 mV), 100 ppm N2O mix flowing
(needle valve at ADM output, 205 Torr), plus a water check point at
nominal 1296.9. Operator control (not in files): switching the supply
N2O -> N2 at nominal 1298 decayed the signal 26 -> 9 mV.

Fit: N2O absorption at 205 Torr (Lorentzian per line, laser Gaussian
FWHM and offset delta grid-searched) + flat baseline, amplitude by
lstsq. Water point excluded from the fit (separate physics: flow-
suppressed water). Concentration derived from the historical R14
responsivity anchor (45 mV / 100 ppm at 600 Torr) is quoted with the
caveat that QTF responsivity rises at lower pressure (Q up), so the
anchor-based number carries ~30-40% systematic.

Output: figures/exp6-r15-line.(png|pdf)
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCAN6 = HERE / "data"
SCAN5 = ROOT / "exp5-sealed-null" / "data"
PAR = ROOT / "hitran" / "h2o_n2o_1295-1300_hitran.par"

P_TORR, T_K = 205.0, 298.0
C_N2O_REF = 100e-6
DAQ_OFFSET_MV = -0.15
R14_MV_PER_100PPM = 45.0              # 600 Torr anchor
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"


def read_point(path):
    wl = power = None
    t, r = [], []
    for line in open(path):
        if line.startswith("#"):
            if "Laser.wavelength" in line:
                wl = float(line.split(",")[1])
            elif "Laser.power" in line:
                power = float(line.split(",")[1])
            continue
        if line.startswith("iso_time"):
            continue
        p = line.strip().split(",")
        if len(p) >= 10:
            t.append(float(p[2]))
            r.append(float(p[9]) * 1000.0)
    t, r = np.array(t), np.array(r)
    core = r[t > 10.0]
    return wl, np.median(core), core.std(), power


pts = sorted(read_point(f) for f in SCAN6.glob("qepas_*.csv"))
nu = np.array([p[0] for p in pts])
r = np.array([p[1] for p in pts]) - DAQ_OFFSET_MV
rs = np.array([p[2] for p in pts])
m_fit = nu > 1297.0                    # exclude the 1296.9 water point
nuf, rf = nu[m_fit], r[m_fit]

lines = []
for l in open(PAR):
    if len(l) < 120:
        continue
    if int(l[0:2]) == 4:
        lines.append((float(l[3:15]), float(l[15:25]), float(l[35:40])))

grid = np.arange(1295.5, 1300.5, 0.002)
a_n = np.zeros_like(grid)
for nu0, S, g_air in lines:
    g = max(g_air * (P_TORR / 760.0), 0.006)      # ~Doppler floor
    a_n += S * C_N2O_REF * N_TOT * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))


def convolved(w):
    sig = w / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a_n, k / k.sum(), mode="same")


best = None
for w in np.arange(0.10, 0.50, 0.01):
    cn = convolved(w)
    for d in np.arange(-0.50, 0.11, 0.005):
        mn = np.interp(nuf + d, grid, cn)
        A = np.column_stack([np.ones_like(nuf), mn])
        coef, *_ = np.linalg.lstsq(A, rf, rcond=None)
        sse = ((rf - A @ coef) ** 2).sum()
        if best is None or sse < best[0]:
            best = (sse, d, w, coef, A)
sse, d, w, (c0, B), A = best
r2 = 1 - sse / ((rf - rf.mean()) ** 2).sum()
cov = sse / (len(rf) - 2) * np.linalg.inv(A.T @ A)
eB = np.sqrt(cov[1, 1])

# concentration via the 600-Torr anchor (systematic: Q rises at low P)
g600 = np.zeros_like(grid)
for nu0, S, g_air in lines:
    g = max(g_air, 0.02) * (600.0 / 760.0)
    g600 += S * C_N2O_REF * (600.0 / 760.0) * 101325 / (1.380649e-23 * T_K) \
        * 1e-6 * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
sig = 0.26 / 2.3548 / 0.002
n = int(6 * sig) + 1
k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
cn600 = np.convolve(g600, k / k.sum(), mode="same")
B_resp = R14_MV_PER_100PPM / np.interp(1297.0501, grid, cn600)
ppm = B / B_resp * 100.0

pk = np.interp(1297.8314 - d, nuf if False else nu, r)
print(f"fit: delta = {d:+.3f} (R15 at nominal {1297.8314 - d:.2f}), "
      f"laser FWHM = {w:.2f} cm-1, R^2 = {r2:.4f}")
print(f"     baseline {c0:.1f} mV; amplitude {B:.2f} +- {eB:.2f} x model")
print(f"     anchor-based concentration ~ {ppm:.0f} ppm "
      f"(nominal 100; +30-40% systematic from Q(205 Torr) > Q(600 Torr))")

# ---- figure -----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.0, 5.0))
fig.patch.set_facecolor("white")

nu_c = np.arange(1297.35, 1298.65, 0.005)
fit_c = c0 + B * np.interp(nu_c + d, grid, convolved(w))
ax.plot(nu_c, fit_c, color=BLUE, lw=1.8,
        label=f"HITRAN N$_2$O fit (205 Torr, laser FWHM {w:.2f} cm$^{{-1}}$)",
        zorder=2)
ax.errorbar(nuf, rf, yerr=rs[m_fit], fmt="o", ms=5, color=INK, mfc=ORANGE,
            mew=0.9, elinewidth=1.0, capsize=2.0,
            label="measured, 100 ppm N$_2$O, constant flow, 205 Torr", zorder=3)

# exp5 sealed-fill contrast (same nominal window)
p5 = sorted(read_point(f) for f in SCAN5.glob("qepas_*_N2O_*.csv"))
nu5 = np.array([p[0] for p in p5])
r5 = np.array([p[1] for p in p5]) - DAQ_OFFSET_MV
m5 = (nu5 >= 1297.4) & (nu5 <= 1298.15)
ax.plot(nu5[m5], r5[m5], "s", ms=4, color=MUTED, mfc="white", mew=1.0,
        label="31 Jul: same cylinder, sealed fill 600 Torr (no delivery)",
        zorder=2)

ax.annotate("R15", (1297.8314 - d, c0 + B * np.interp(1297.8314, grid,
            convolved(w)) + 1.2), ha="center", fontsize=9, color=BLUE)
ax.annotate("supply switched N$_2$O $\\rightarrow$ N$_2$ at nominal 1298:\n"
            "signal 26 $\\rightarrow$ 9 mV (gas-exchange control)",
            (0.02, 0.97), xycoords="axes fraction", va="top", fontsize=8,
            color=MUTED)

ax.set_xlabel(r"nominal set point (cm$^{-1}$)")
ax.set_ylabel("QEPAS signal $R$ (mV)")
ax.set_xlim(1297.4, 1298.6)
ax.set_ylim(0, 34)
ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_formatter("{x:.1f}")
ax.grid(True, axis="both", which="major", alpha=0.18, lw=0.5)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(labelsize=8.5, color=MUTED)
ax.legend(loc="upper right", frameon=False, fontsize=8)
ax.set_title("N$_2$O detected — R15 line, 3 Aug 2026 "
             f"($\\delta$ = {d:+.2f}, R$^2$ = {r2:.3f}, "
             "first detection since Dec 2025)", fontsize=10.5, color=INK)

fig.tight_layout()
out = HERE / "exp6-r15-line"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"wrote {out}.png/.pdf")
