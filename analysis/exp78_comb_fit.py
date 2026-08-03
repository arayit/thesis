#!/usr/bin/env python3
"""Exp7/exp8 (3 Aug 2026): blank vs 100 ppm N2O full-window scans at
205 Torr constant flow — the complete R-branch comb.

exp7: pure N2 blank, nominal 1295.0-1300.0, 0.1 steps, 30 s/point,
      ~200 Torr, 10 sccm constant flow. Closing anchor at 1295.0
      (drift +0.25 mV over 42 min). Lab: 21 C, 75% RH (operator note).
exp8: same grid with the 100 ppm N2O mix. Closing anchor -0.46 mV.
      Metadata correction: gas_type in some early exp8 files reads "N2"
      (logger field not updated at the session start); the flowing gas
      was the N2O mix throughout — identity taken from the experiment,
      not the header. First ~2 points carry a small equilibration
      transient after the gas switch.

Fits:
1. exp8 full model: H2O + N2O (205 Torr Lorentzian x Gaussian laser)
   + linear baseline; (delta, FWHM) grid-searched.
2. Difference exp8-exp7: N2O-only + flat offset — the water background
   and optical floor cancel point-by-point.

Output: figures/exp78-comb.(png|pdf)
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parent.parent
S7 = ROOT / "experimental" / "daq" / "2026-08-03" / "exp7-scan"
S8 = ROOT / "experimental" / "daq" / "2026-08-03" / "exp8-scan"
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1295-1300_hitran.par"

P_TORR, T_K = 205.0, 294.0
C_N2O_REF = 100e-6
C_H2O_REF = 23.76 / P_TORR            # nominal reference; amplitude free
DAQ_OFFSET_MV = -0.15
R14_MV_PER_100PPM = 45.0              # 600 Torr anchor (Q systematic at 205)
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"
PICKETS = {"R11": 1294.6845, "R12": 1295.4766, "R13": 1296.2651,
           "R14": 1297.0501, "R15": 1297.8314, "R16": 1298.6093,
           "R17": 1299.3835}


def read_point(path):
    wl = power = start = None
    t, r = [], []
    for line in open(path):
        if line.startswith("#"):
            if "Laser.wavelength" in line:
                wl = float(line.split(",")[1])
            elif "Laser.power" in line:
                power = float(line.split(",")[1])
            elif "start," in line:
                start = line.split(",")[1].strip()
            continue
        if line.startswith("iso_time"):
            continue
        p = line.strip().split(",")
        if len(p) >= 10:
            t.append(float(p[2]))
            r.append(float(p[9]) * 1000.0)
    t, r = np.array(t), np.array(r)
    core = r[t > 10.0]
    return start, wl, np.median(core), core.std(), power


def load(folder):
    pts = sorted(read_point(f) for f in folder.glob("qepas_*.csv"))
    scan, anchor = pts[:-1], pts[-1]          # last file = 1295.0 re-measure
    nu = np.array([p[1] for p in scan])
    r = np.array([p[2] for p in scan]) - DAQ_OFFSET_MV
    rs = np.array([p[3] for p in scan])
    pw = np.array([p[4] for p in scan])
    return nu, r * (pw.mean() / pw), rs, anchor


nu7, r7, s7, a7 = load(S7)
nu8, r8, s8, a8 = load(S8)
diff = r8 - r7                                 # same grid by construction
sd = np.sqrt(s7 ** 2 + s8 ** 2)
print(f"anchors: exp7 {a7[2] - r7[0]:+.2f} mV, exp8 {a8[2] - r8[0]:+.2f} mV")

lines = {1: [], 4: []}
for l in open(PAR):
    if len(l) < 120:
        continue
    mol = int(l[0:2])
    if mol in lines:
        lines[mol].append((float(l[3:15]), float(l[15:25]), float(l[35:40])))

grid = np.arange(1293.5, 1301.5, 0.002)


def alpha(mol, conc):
    a = np.zeros_like(grid)
    for nu0, S, g_air in lines[mol]:
        g = max(g_air * (P_TORR / 760.0), 0.006)
        a += S * conc * N_TOT * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
    return a


def convolved(a, w):
    sig = w / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a, k / k.sum(), mode="same")


a_w, a_n = alpha(1, C_H2O_REF), alpha(4, C_N2O_REF)

# --- fit 1: exp8 full model --------------------------------------------------
best = None
for w in np.arange(0.14, 0.42, 0.01):
    cw, cn = convolved(a_w, w), convolved(a_n, w)
    for d in np.arange(-0.45, 0.05, 0.005):
        mw = np.interp(nu8 + d, grid, cw)
        mn = np.interp(nu8 + d, grid, cn)
        A = np.column_stack([np.ones_like(nu8), nu8 - nu8.mean(), mw, mn])
        coef, *_ = np.linalg.lstsq(A, r8, rcond=None)
        sse = ((r8 - A @ coef) ** 2).sum()
        if best is None or sse < best[0]:
            best = (sse, d, w, coef)
sse8, d8, w8, (c0, c1, Bw, Bn) = best
r2_8 = 1 - sse8 / ((r8 - r8.mean()) ** 2).sum()

# --- fit 2: difference, N2O only --------------------------------------------
best = None
for w in np.arange(0.14, 0.42, 0.01):
    cn = convolved(a_n, w)
    for d in np.arange(-0.45, 0.05, 0.005):
        mn = np.interp(nu8 + d, grid, cn)
        A = np.column_stack([np.ones_like(nu8), mn])
        coef, *_ = np.linalg.lstsq(A, diff, rcond=None)
        sse = ((diff - A @ coef) ** 2).sum()
        if best is None or sse < best[0]:
            best = (sse, d, w, coef, A)
sseD, dD, wD, (cD, BD), AD = best
r2_D = 1 - sseD / ((diff - diff.mean()) ** 2).sum()
covD = sseD / (len(diff) - 2) * np.linalg.inv(AD.T @ AD)
eBD = np.sqrt(covD[1, 1])

# anchor-based concentration (600 Torr anchor; Q(205)>Q(600) systematic)
g600 = alpha(4, C_N2O_REF) * 0  # rebuild at 600 Torr
N600 = (600.0 / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6
for nu0, S, g_air in lines[4]:
    g = max(g_air, 0.02) * (600.0 / 760.0)
    g600 += S * C_N2O_REF * N600 * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
cn600 = convolved(g600, 0.26)
B_resp = R14_MV_PER_100PPM / np.interp(1297.0501, grid, cn600)
print(f"exp8 full fit : delta={d8:+.3f}, FWHM={w8:.2f}, R2={r2_8:.4f}")
print(f"diff comb fit : delta={dD:+.3f}, FWHM={wD:.2f}, R2={r2_D:.4f}; "
      f"amplitude {BD / B_resp * 100:.0f} +- {eBD / B_resp * 100:.0f} ppm-equiv "
      f"(600-Torr anchor; Q systematic ~+25-40%)")

# --- figure ------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(10.0, 7.0), sharex=True,
    gridspec_kw={"height_ratios": [1.4, 1.0], "hspace": 0.10})
fig.patch.set_facecolor("white")

nu_f = np.arange(1295.0, 1300.001, 0.005)
fit8 = c0 + c1 * (nu_f - nu8.mean()) + Bw * np.interp(
    nu_f + d8, grid, convolved(a_w, w8)) + Bn * np.interp(
    nu_f + d8, grid, convolved(a_n, w8))

ax1.plot(nu_f, fit8, color=BLUE, lw=1.5,
         label="HITRAN fit (N$_2$O + H$_2$O, 205 Torr)", zorder=2)
ax1.plot(nu7, r7, "s-", ms=3.5, lw=0.7, color=MUTED, mfc="white", mew=0.9,
         label="exp7: pure N$_2$ blank", zorder=3)
ax1.errorbar(nu8, r8, yerr=s8, fmt="o", ms=4.2, color=INK, mfc=ORANGE,
             mew=0.8, elinewidth=0.8, capsize=1.5,
             label="exp8: 100 ppm N$_2$O mix", zorder=4)
ax1.set_ylabel("QEPAS signal $R$ (mV)")
ax1.set_ylim(0, 33)
ax1.legend(loc="upper right", frameon=False, fontsize=8.5, ncols=1)
ax1.set_title("N$_2$O R-branch comb, 3 Aug 2026 — 205 Torr constant flow, "
              f"$\\delta$ = {dD:+.2f}, diff-fit R$^2$ = {r2_D:.3f}",
              fontsize=10.5, color=INK)

fitD = cD + BD * np.interp(nu_f + dD, grid, convolved(a_n, wD))
ax2.plot(nu_f, fitD, color=BLUE, lw=1.5, label="HITRAN N$_2$O only", zorder=2)
ax2.errorbar(nu8, diff, yerr=sd, fmt="o", ms=4.2, color=INK, mfc="white",
             mew=1.0, elinewidth=0.8, capsize=1.5,
             label="exp8 $-$ exp7 (water + background cancel)", zorder=3)
for name, act in PICKETS.items():
    nom = act - dD
    if 1295.05 < nom < 1299.95:
        v = cD + BD * np.interp(act, grid, convolved(a_n, wD))
        ax2.annotate(name, (nom, v + 1.3), ha="center", fontsize=8,
                     color=BLUE)
ax2.set_ylabel(r"$\Delta R$ (mV)")
ax2.set_xlabel(r"nominal set point (cm$^{-1}$)")
ax2.set_ylim(-2, 26)
ax2.legend(loc="upper left", frameon=False, fontsize=8.5)

for ax in (ax1, ax2):
    ax.set_xlim(1294.9, 1300.1)
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_formatter("{x:.1f}")
    ax.grid(True, axis="x", which="minor", alpha=0.10, lw=0.4)
    ax.grid(True, axis="both", which="major", alpha=0.18, lw=0.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8.5, color=MUTED)

fig.tight_layout()
out = ROOT / "figures" / "exp78-comb"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"wrote {out}.png/.pdf")
