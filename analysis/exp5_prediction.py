#!/usr/bin/env python3
"""Registered prediction for exp5: the 100 ppm N2O counterpart scan.

Committed BEFORE the experiment. Uses only quantities already fitted
from the 28-Jul pure-N2 scan (exp4): delta = -0.23, laser FWHM = 0.26,
the water-only fit (baseline + water amplitude) and the historical R14
responsivity anchor for the N2O amplitude. Prediction:

  R_pred(nu_nom) = [exp4 water-only fit] + B_resp * conv[alpha_N2O_100ppm]

evaluated at the same 51 nominal set points 1295.0-1300.0. If the new
scan lands on this curve, N2O detection is demonstrated against a
pre-registered quantitative prediction, not a post-hoc fit.

Assumptions that can shift the outcome (stated in advance):
- delta is per-session; if it moved, the whole comb shifts rigidly in
  nominal position but keeps the 0.78 cm-1 spacing (the fingerprint).
- The optical background floor drifts (documented 0-13 mV); a flat
  offset between prediction and measurement is expected at that scale.
- B_resp comes from a different day/alignment (+-30%); picket heights
  carry that uncertainty, positions and spacing do not.

Output: figures/exp5-scan-prediction.(png|pdf) + checkpoint table.
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parent.parent
SCAN = ROOT / "experimental" / "daq" / "2026-07-28" / "exp4-scan"
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1295-1300_hitran.par"

P_TORR, T_K = 600.0, 298.0
C_N2O_REF = 100e-6
C_H2O_REF = 23.76 / P_TORR
DAQ_OFFSET_MV = -0.15
R14_MV_PER_100PPM = 45.0
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"

N2O_NOMINAL = {  # actual line -> nominal at delta = -0.23
    "R12": 1295.4766, "R13": 1296.2651, "R14": 1297.0501,
    "R15": 1297.8314, "R16": 1298.6093, "R17": 1299.3835,
}


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


files = sorted(SCAN.glob("qepas_*_N2_*.csv"))
pts = sorted(read_point(f) for f in files)
nu = np.array([p[0] for p in pts])
r_raw = np.array([p[1] for p in pts]) - DAQ_OFFSET_MV
power = np.array([p[3] for p in pts])
r = r_raw * (power.mean() / power)

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
        g = max(g_air, 0.02) * (P_TORR / 760.0)
        a += S * conc * N_TOT * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
    return a


def convolved(a, w_fwhm):
    sig = w_fwhm / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a, k / k.sum(), mode="same")


a_w, a_n = alpha(1, C_H2O_REF), alpha(4, C_N2O_REF)

# reproduce the exp4 water-only fit exactly (same grid search)
best_w = None
for w2 in np.arange(0.06, 0.62, 0.02):
    cw = convolved(a_w, w2)
    for d2 in np.arange(-0.50, 0.31, 0.005):
        mw = np.interp(nu + d2, grid, cw)
        A = np.column_stack([np.ones_like(nu), nu - nu.mean(), mw])
        coef, *_ = np.linalg.lstsq(A, r, rcond=None)
        sse2 = ((r - A @ coef) ** 2).sum()
        if best_w is None or sse2 < best_w[0]:
            best_w = (sse2, d2, w2, coef)
_, d_w, w_w, (c0w, c1w, Bw_w) = best_w
print(f"exp4 water fit reproduced: delta {d_w:+.3f}, FWHM {w_w:.2f}")

cn_pk = np.interp(1297.0501, grid, convolved(a_n, w_w))
B_resp = R14_MV_PER_100PPM / cn_pk

nu_f = np.arange(1295.0, 1300.001, 0.01)
water_f = c0w + c1w * (nu_f - nu.mean()) + Bw_w * np.interp(
    nu_f + d_w, grid, convolved(a_w, w_w))
n2o_f = B_resp * np.interp(nu_f + d_w, grid, convolved(a_n, w_w))
pred_f = water_f + n2o_f

print("\ncheckpoints (nominal -> predicted mV with 100 ppm N2O):")
for name, act in N2O_NOMINAL.items():
    nom = act - d_w
    v = np.interp(nom, nu_f, pred_f)
    print(f"  {name}: actual {act:.4f} -> nominal {nom:.2f}  ~{v:.0f} mV")
for nom in (1297.65, 1298.45, 1299.20):   # valleys between pickets
    print(f"  valley at nominal {nom:.2f}: ~{np.interp(nom, nu_f, pred_f):.0f} mV")

fig, ax = plt.subplots(figsize=(9.5, 4.8))
fig.patch.set_facecolor("white")

ax.plot(nu, r, "o", ms=4.0, color=MUTED, mfc="white", mew=1.1,
        label="measured 28 Jul (pure N$_2$) — exp4", zorder=2)
ax.plot(nu_f, water_f, color=ORANGE, lw=1.4, ls="--",
        label="exp4 water fit (unchanged background)", zorder=3)
ax.plot(nu_f, pred_f, color=BLUE, lw=1.8,
        label="PREDICTION: same scan with 100 ppm N$_2$O", zorder=4)

for name, act in N2O_NOMINAL.items():
    nom = act - d_w
    v = np.interp(nom, nu_f, pred_f)
    ax.annotate(name, (nom, v + 1.5), ha="center", fontsize=8, color=BLUE)

ax.set_xlabel(r"nominal set point (cm$^{-1}$)")
ax.set_ylabel("QEPAS signal $R$ (mV)")
ax.set_xlim(1294.9, 1300.1)
ax.set_ylim(0, 80)
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_formatter("{x:.1f}")
ax.grid(True, axis="x", which="minor", alpha=0.10, lw=0.4)
ax.grid(True, axis="both", which="major", alpha=0.18, lw=0.5)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(labelsize=8.5, color=MUTED)
ax.legend(loc="upper left", frameon=False, fontsize=8.5)
ax.set_title("Registered prediction for the 100 ppm N$_2$O counterpart scan "
             f"(exp4 parameters: $\\delta$ = {d_w:+.2f}, FWHM = {w_w:.2f}, "
             "$B$ from R14 anchor)", fontsize=10, color=INK)

fig.tight_layout()
out = ROOT / "figures" / "exp5-scan-prediction"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"\nwrote {out}.png/.pdf")
