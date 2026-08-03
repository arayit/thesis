#!/usr/bin/env python3
"""Exp5 (31 Jul 2026): the 100 ppm N2O counterpart scan vs exp4 and the
registered prediction.

Input: experimental/daq/2026-07-31/exp5-scan/qepas_*_N2O_*.csv — 32 points,
nominal 1295.0-1298.1, 0.1 steps, sealed 600 Torr, fill drawn from the
"100 ppm N2O" cylinder after pump-down through the ADM output valve.

Analysis:
1. Same full fit as exp4 (H2O + N2O + linear baseline; delta, laser FWHM
   grid-searched) -> today's delta, FWHM, water amount, fitted N2O ppm.
2. Comb-template correlation on the point-by-point difference exp5-exp4:
   regress the difference onto the predicted 100-ppm comb shape -> picket
   amplitude in mV with 1-sigma error -> N2O concentration bound that is
   robust to the shared water background and slow drift.

Result (31 Jul): delta=-0.240, FWHM=0.26, water=1.07x saturation --
the instrument state reproduced exp4 within noise. N2O in the chamber:
comb amplitude -0.67 +- 0.48 mV = -1.5 +- 1.1 ppm (consistent with zero;
<= ~3 ppm at 3 sigma). The gas delivered to the ADM was spectroscopically
wet N2, not a 100 ppm N2O mix.

Output: figures/exp5-vs-exp4.(png|pdf)
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parent.parent
SCAN5 = ROOT / "experimental" / "daq" / "2026-07-31" / "exp5-scan"
SCAN4 = ROOT / "experimental" / "daq" / "2026-07-28" / "exp4-scan"
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1295-1300_hitran.par"

P_TORR, T_K = 600.0, 298.0
C_N2O_REF = 100e-6
C_H2O_REF = 23.76 / P_TORR
DAQ_OFFSET_MV = -0.15
R14_MV_PER_100PPM = 45.0
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


def load(folder, tag):
    pts = sorted(read_point(f) for f in folder.glob(f"qepas_*_{tag}_*.csv"))
    nu = np.array([p[0] for p in pts])
    r = np.array([p[1] for p in pts]) - DAQ_OFFSET_MV
    pw = np.array([p[3] for p in pts])
    return nu, r * (pw.mean() / pw), np.array([p[2] for p in pts])


nu5, r5, s5 = load(SCAN5, "N2O")
nu4, r4, s4 = load(SCAN4, "N2")
print(f"exp5: {len(nu5)} pts {nu5[0]:.1f}-{nu5[-1]:.1f}; exp4: {len(nu4)} pts")

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


def full_fit(nu, r):
    best = None
    for w in np.arange(0.06, 0.62, 0.02):
        cw, cn = convolved(a_w, w), convolved(a_n, w)
        for d in np.arange(-0.50, 0.31, 0.005):
            mw = np.interp(nu + d, grid, cw)
            mn = np.interp(nu + d, grid, cn)
            A = np.column_stack([np.ones_like(nu), nu - nu.mean(), mw, mn])
            coef, *_ = np.linalg.lstsq(A, r, rcond=None)
            sse = ((r - A @ coef) ** 2).sum()
            if best is None or sse < best[0]:
                best = (sse, d, w, coef, A)
    sse, d, w, coef, A = best
    cov = sse / (len(r) - 4) * np.linalg.inv(A.T @ A)
    return d, w, coef, np.sqrt(np.diag(cov)), 1 - sse / ((r - r.mean()) ** 2).sum()


for name, nu, r in [("exp4", nu4, r4), ("exp5", nu5, r5)]:
    d, w, (c0, c1, Bw, Bn), (e0, e1, eW, eN), r2 = full_fit(nu, r)
    B_resp = R14_MV_PER_100PPM / np.interp(1297.0501, grid, convolved(a_n, w))
    print(f"{name}: delta={d:+.3f} FWHM={w:.2f} R2={r2:.4f}  "
          f"water={Bw / B_resp:.3f}+-{eW / B_resp:.3f} x sat  "
          f"N2O={Bn / B_resp * 100:.2f}+-{eN / B_resp * 100:.2f} ppm")
    if name == "exp5":
        d5, w5 = d, w

# comb correlation on the difference (shared water background cancels)
common = np.intersect1d(np.round(nu5, 1), np.round(nu4, 1))
i5 = [list(np.round(nu5, 1)).index(x) for x in common]
i4 = [list(np.round(nu4, 1)).index(x) for x in common]
diff = r5[i5] - r4[i4]
cn = convolved(a_n, 0.26)
T = np.interp(common + d5, grid, cn)
T45 = T * (R14_MV_PER_100PPM / np.interp(1297.0501, grid, cn))
A = np.column_stack([np.ones_like(common), common - common.mean(), T45 / T45.max()])
coef, *_ = np.linalg.lstsq(A, diff, rcond=None)
res = diff - A @ coef
cov = (res ** 2).sum() / (len(diff) - 3) * np.linalg.inv(A.T @ A)
amp, err = coef[2], np.sqrt(cov[2, 2])
print(f"comb in (exp5-exp4): {amp:.2f} +- {err:.2f} mV pickets "
      f"= {amp / 45 * 100:.2f} +- {err / 45 * 100:.2f} ppm N2O")

# ---- figure -----------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(9.5, 6.6), sharex=True,
    gridspec_kw={"height_ratios": [2.4, 1.0], "hspace": 0.08})
fig.patch.set_facecolor("white")

nu_f = np.arange(1295.0, 1300.001, 0.01)
# registered prediction (exp4 water fit + 100 ppm comb via anchor)
bw = full_fit(nu4, r4)
d4b, w4b, (c04, c14, Bw4, Bn4) = bw[0], bw[1], bw[2]
B_resp = R14_MV_PER_100PPM / np.interp(1297.0501, grid, convolved(a_n, w4b))
water_f = c04 + c14 * (nu_f - nu4.mean()) + Bw4 * np.interp(
    nu_f + d4b, grid, convolved(a_w, w4b))
pred_f = water_f + B_resp * np.interp(nu_f + d4b, grid, convolved(a_n, w4b))

ax1.plot(nu_f, pred_f, color=BLUE, lw=1.6, ls="--", alpha=0.8,
         label="registered prediction IF 100 ppm N$_2$O present", zorder=2)
ax1.plot(nu4, r4, "o", ms=4.0, color=MUTED, mfc="white", mew=1.1,
         label="exp4, 28 Jul (pure N$_2$)", zorder=3)
ax1.errorbar(nu5, r5, yerr=s5, fmt="o", ms=4.5, color=INK, mfc=ORANGE,
             mew=0.8, elinewidth=0.9, capsize=1.8,
             label='exp5, 31 Jul (fill from the "100 ppm N$_2$O" cylinder)',
             zorder=4)
ax1.set_ylabel("QEPAS signal $R$ (mV)")
ax1.set_ylim(0, 80)
ax1.legend(loc="upper right", frameon=False, fontsize=8.5)
ax1.set_title("Exp5 vs exp4 vs prediction — measured N$_2$O in chamber: "
              "$-1.5\\pm1.1$ ppm (consistent with zero; $\\leq$3 ppm at "
              "3$\\sigma$)", fontsize=10.5, color=INK)

ax2.axhspan(-3 * 0.45, 3 * 0.45, color=MUTED, alpha=0.12, lw=0)
ax2.plot(common, diff, "o-", ms=3.5, lw=0.8, color=INK, mfc="white",
         label="exp5 $-$ exp4 (measured)")
ax2.plot(common, T45 - T45.max() * 0 + 0 * common - (T45.mean()), lw=0)  # spacer
ax2.plot(common, T45, color=BLUE, lw=1.4, ls="--",
         label="what 100 ppm would add")
ax2.annotate("shaded: $\\pm$3 ppm equivalent", (1295.05, 1.7), fontsize=7.5,
             color=MUTED)
ax2.set_ylabel("$\\Delta R$ (mV)")
ax2.set_xlabel(r"nominal set point (cm$^{-1}$)")
ax2.set_ylim(-6, 50)
ax2.legend(loc="upper right", frameon=False, fontsize=8)

for ax in (ax1, ax2):
    ax.set_xlim(1294.9, 1298.6)
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_formatter("{x:.1f}")
    ax.grid(True, axis="x", which="minor", alpha=0.10, lw=0.4)
    ax.grid(True, axis="both", which="major", alpha=0.18, lw=0.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8.5, color=MUTED)

fig.tight_layout()
out = ROOT / "figures" / "exp5-vs-exp4"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"wrote {out}.png/.pdf")
