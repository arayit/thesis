#!/usr/bin/env python3
"""Fit the 28-Jul-2026 pure-N2 wavelength scan (exp4) against HITRAN.

Input: experimental/daq/2026-07-28/exp4-scan/qepas_*_N2_*.csv — one 30 s
logger file per nominal set point, 1295.0-1300.0 in 0.1 steps, sealed
chamber at 600 Torr, TC 3 s, sens 200 mV.

Model:  R(nu_nom) = c0 + c1*(nu_nom - <nu>)
                  + B_w * conv[alpha_H2O](nu_nom + delta)
                  + B_n * conv[alpha_N2O](nu_nom + delta)

alpha curves from data/hitran/h2o_n2o_1295-1300_hitran.par at 600 Torr:
H2O scaled to saturation at 25 C (3.96%), N2O to 100 ppm, Lorentzian
pressure broadening, then convolved with a Gaussian laser lineshape of
FWHM w. (delta, w) are grid-searched; (c0, c1, B_w, B_n) solved by
linear least squares at each grid point.

If both species were present at exactly the reference concentrations,
B_w = B_n = the instrument responsivity in mV per cm^-1 of alpha. The
ratio B_w/B_resp (B_resp anchored by the 100 ppm N2O ~45 mV @ R14
history) estimates the actual water fraction relative to saturation.

Outputs: figures/exp4-scan-fit.(png|pdf) + fit table on stdout.
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCAN = HERE / "data"
PAR = ROOT / "hitran" / "h2o_n2o_1295-1300_hitran.par"

P_TORR, T_K = 600.0, 298.0
C_N2O_REF = 100e-6                    # reference: 100 ppm
C_H2O_REF = 23.76 / P_TORR            # reference: saturation at 25 C (3.96%)
DAQ_OFFSET_MV = -0.15                 # CH1/DAQ zero (beam-block test, 20 Jul)
R14_MV_PER_100PPM = 45.0              # historical 100 ppm N2O level at R14, ~3.2 mW
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6  # molec/cm^3

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"

N2O_PICKETS = [1295.4766, 1296.2651, 1297.0501, 1297.8314, 1298.6093, 1299.3835]
H2O_MAIN = [1296.4901, 1296.7093, 1297.1837]


# ---- measured spectrum ------------------------------------------------------
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
            r.append(float(p[9]) * 1000.0)          # r_v (V) -> mV
    t, r = np.array(t), np.array(r)
    core = r[t > 10.0]                              # drop TC settling
    return wl, np.median(core), core.std(), power


files = sorted(SCAN.glob("qepas_*_N2_*.csv"))
pts = sorted(read_point(f) for f in files)
nu = np.array([p[0] for p in pts])
r_raw = np.array([p[1] for p in pts]) - DAQ_OFFSET_MV
r_std = np.array([p[2] for p in pts])
power = np.array([p[3] for p in pts])
r = r_raw * (power.mean() / power)                  # normalize to mean power
print(f"{len(nu)} points, {nu[0]:.1f}-{nu[-1]:.1f}; power {power.min():.2f}-"
      f"{power.max():.2f} mW; per-point std {r_std.mean():.2f} mV")

# ---- HITRAN model curves ----------------------------------------------------
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


a_w, a_n = alpha(1, C_H2O_REF), alpha(4, C_N2O_REF)


def convolved(a, w_fwhm):
    sig = w_fwhm / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a, k / k.sum(), mode="same")


# ---- grid search (delta, w) + linear lstsq ----------------------------------
best = None
for w in np.arange(0.06, 0.62, 0.02):
    cw, cn = convolved(a_w, w), convolved(a_n, w)
    for d in np.arange(-0.50, 0.31, 0.005):
        mw = np.interp(nu + d, grid, cw)
        mn = np.interp(nu + d, grid, cn)
        A = np.column_stack([np.ones_like(nu), nu - nu.mean(), mw, mn])
        coef, *_ = np.linalg.lstsq(A, r, rcond=None)
        res = r - A @ coef
        sse = (res ** 2).sum()
        if best is None or sse < best[0]:
            best = (sse, d, w, coef, A @ coef, res)

sse, d, w, (c0, c1, B_w, B_n), model, res = best
r2 = 1 - sse / ((r - r.mean()) ** 2).sum()
rms = np.sqrt(sse / len(nu))

# water amount anchored to the historical N2O responsivity
cn_pk = np.interp(1297.0501, grid, convolved(a_n, w))     # modeled 100 ppm peak
B_resp = R14_MV_PER_100PPM / cn_pk                        # mV per cm^-1
frac_sat = B_w / B_resp
n2o_ppm = B_n / B_resp * 100.0

print(f"\nfit: delta = {d:+.3f} cm-1 (actual = nominal {d:+.3f}), "
      f"laser FWHM = {w:.2f} cm-1")
print(f"     baseline {c0:.2f} mV {c1:+.2f} mV/cm-1;  R^2 = {r2:.4f}, "
      f"residual rms = {rms:.2f} mV")
print(f"     B_w = {B_w:.0f}, B_n = {B_n:.0f} mV/(cm-1)  "
      f"[responsivity anchor {B_resp:.0f}]")
print(f"     -> H2O ~ {frac_sat:.2f} x saturation(25 C) = "
      f"{frac_sat * C_H2O_REF * 100:.1f}% = "
      f"{frac_sat * 23.76:.1f} Torr partial pressure")
print(f"     -> residual N2O equivalent ~ {n2o_ppm:.1f} ppm")

# water-only fit (same grid search, no N2O column) -- this is what gets plotted
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
sse_w, d_w, w_w, (c0w, c1w, Bw_w) = best_w
r2_w = 1 - sse_w / ((r - r.mean()) ** 2).sum()
print(f"     water-only: R^2 = {r2_w:.4f} (delta {d_w:+.3f}, FWHM {w_w:.2f})")

# N2O-only alternate for the record
A2 = np.column_stack([np.ones_like(nu), nu - nu.mean(),
                      np.interp(nu + d, grid, convolved(a_n, w))])
c2, *_ = np.linalg.lstsq(A2, r, rcond=None)
sse2 = ((r - A2 @ c2) ** 2).sum()
print(f"     N2O-only  : R^2 = {1 - sse2 / ((r - r.mean()) ** 2).sum():.4f}")

# ---- figure: measured points + HITRAN water fit -----------------------------
fig, ax1 = plt.subplots(figsize=(9.5, 4.8))
fig.patch.set_facecolor("white")

nu_f = np.arange(1295.0, 1300.001, 0.01)
fit_f = c0w + c1w * (nu_f - nu.mean()) + Bw_w * np.interp(
    nu_f + d_w, grid, convolved(a_w, w_w))

ax1.plot(nu_f, fit_f, color=ORANGE, lw=1.8,
         label="HITRAN H$_2$O fit (600 Torr, Lorentzian $\\times$ laser lineshape)",
         zorder=2)
ax1.errorbar(nu, r, yerr=r_std, fmt="o", ms=4.5, color=INK, mfc="white",
             mew=1.2, elinewidth=1.0, capsize=2.0,
             label="measured (pure N$_2$, sealed, 600 Torr)", zorder=3)

ax1.set_ylabel("QEPAS signal $R$ (mV)")
ax1.set_xlabel(r"nominal set point (cm$^{-1}$)")
ax1.set_ylim(0, 66)
ax1.legend(loc="upper right", frameon=False, fontsize=8.5)
ax1.annotate(
    f"error bars ($\\pm${r_std.mean():.2f} mV plateau std)\nare smaller than the symbols",
    (0.985, 0.72), xycoords="axes fraction", ha="right", fontsize=8, color=MUTED)
ax1.set_title(
    f"Pure-N$_2$ wavelength scan, 28 Jul 2026 — HITRAN water fit  "
    f"($\\delta$ = {d_w:+.2f} cm$^{{-1}}$, laser FWHM = {w_w:.2f} cm$^{{-1}}$, "
    f"R$^2$ = {r2_w:.3f})", fontsize=10.5, color=INK)

for ax in (ax1,):
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
out = HERE / "exp4-scan-fit"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"\nwrote {out}.png/.pdf")
