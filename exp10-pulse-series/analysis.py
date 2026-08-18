#!/usr/bin/env python3
"""Exp10 (17 Aug 2026): pulse-width (power) series on the R15 line.

10 pulse widths, 100-1000 ns, at fixed rep rate 12458.8 Hz = f0;
per width a 6-7 point mini-profile across R15 (nominal 1297.7-1298.3),
100 ppm N2O in constant flow at 199 Torr. Each profile is fitted with
the HITRAN N2O model (199 Torr Lorentzian x Gaussian laser lineshape,
flat local baseline): free amplitude, offset, center shift d(tau) and
effective laser FWHM w(tau).

Outputs:
- figures/thesis/fig-power-linearity: R15 line area vs measured average
  power (area is lineshape-independent, so chirp broadening does not
  alias into the linearity test) + fit through origin.
- figures/thesis/fig-pulse-characterization: P_peak, line-center shift,
  and effective laser FWHM vs pulse width (3 stacked panels).
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCAN = HERE / "data"
PAR = ROOT / "hitran" / "h2o_n2o_1111-2000_hitran.par"

P_TORR, T_K = 199.0, 296.0
C_N2O_REF = 100e-6
DAQ_OFFSET_MV = -0.15
F_REP = 12458.8
R15 = 1297.8314
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"

plt.rcParams.update({
    "font.size": 9.5, "axes.labelsize": 10, "legend.fontsize": 9,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
    "axes.spines.top": False, "axes.spines.right": False,
})


def read_point(path):
    wl = pw = tau = None
    t, r = [], []
    for line in open(path):
        if line.startswith("#"):
            if "Laser.wavelength" in line:
                wl = float(line.split(",")[1])
            elif "Laser.power" in line:
                pw = float(line.split(",")[1])
            elif "pulse_width" in line:
                tau = float(line.split(",")[1])
            continue
        if line.startswith("iso_time"):
            continue
        p = line.strip().split(",")
        if len(p) >= 10:
            t.append(float(p[2]))
            r.append(float(p[9]) * 1000.0)
    t, r = np.array(t), np.array(r)
    core = r[t > 10.0]
    return tau, wl, np.median(core), core.std(), pw


lines = []
for l in open(PAR):
    if len(l) < 120:
        continue
    if int(l[0:2]) == 4:
        nu0 = float(l[3:15])
        if 1290.0 < nu0 < 1305.0:
            lines.append((nu0, float(l[15:25]), float(l[35:40])))

grid = np.arange(1294.5, 1301.5, 0.002)
a_n = np.zeros_like(grid)
for nu0, S, g_air in lines:
    g = max(g_air * (P_TORR / 760.0), 0.006)
    a_n += S * C_N2O_REF * N_TOT * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
# R15-only unit-area reference for the area scale
iR15 = np.argmin([abs(x[0] - R15) if x[1] > 1e-19 else 9 for x in lines])
S15 = max(S for nu0, S, g in lines if abs(nu0 - R15) < 2e-3)
AREA15 = S15 * C_N2O_REF * N_TOT          # cm^-1 * cm^-1 (integrated alpha)


def convolved(w):
    sig = w / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a_n, k / k.sum(), mode="same")


pts = sorted(read_point(f) for f in SCAN.glob("qepas_*.csv"))
taus = sorted(set(p[0] for p in pts))
rows = []
print(f"{'tau':>5} {'n':>2} {'P mW':>5} {'peak mV':>8} {'center':>9} "
      f"{'FWHM':>5} {'area rel':>8}")
for tau in taus:
    g = [p for p in pts if p[0] == tau]
    nu = np.array([p[1] for p in g])
    r = np.array([p[2] for p in g]) - DAQ_OFFSET_MV
    P = np.mean([p[4] for p in g])
    best = None
    for w in np.arange(0.06, 0.62, 0.01):
        cn = convolved(w)
        for d in np.arange(-0.45, 0.10, 0.005):
            mn = np.interp(nu + d, grid, cn)
            A = np.column_stack([np.ones_like(nu), mn])
            coef, *_ = np.linalg.lstsq(A, r, rcond=None)
            sse = ((r - A @ coef) ** 2).sum()
            if best is None or sse < best[0]:
                best = (sse, d, w, coef)
    sse, d, w, (c0, B) = best
    peak = B * np.interp(R15, grid, convolved(w))
    area = B * AREA15                      # mV * cm^-1, lineshape-free
    rows.append((tau, P, peak, R15 - d, w, area, c0))
    print(f"{tau:5.0f} {len(g):2d} {P:5.2f} {peak:8.2f} {R15 - d:9.3f} "
          f"{w:5.2f} {area:8.3f}")

tau_a = np.array([r[0] for r in rows])
P_a = np.array([r[1] for r in rows])
peak_a = np.array([r[2] for r in rows])
cen_a = np.array([r[3] for r in rows])
w_a = np.array([r[4] for r in rows])
area_a = np.array([r[5] for r in rows])

duty = tau_a * 1e-9 * F_REP
ppeak = P_a / duty                          # mW peak power

k_lin = (area_a * P_a).sum() / (P_a ** 2).sum()   # through-origin fit
res = area_a - k_lin * P_a
print(f"\nthrough-origin fit: area = {k_lin:.4f} x P_avg;  "
      f"rms dev {100 * res.std() / area_a.mean():.1f}% of mean")
print(f"P_peak: {ppeak[0]:.0f} mW @100ns -> {ppeak[-1]:.0f} mW @1000ns "
      f"({100 * (ppeak[-1] / ppeak[0] - 1):+.0f}% rollover)")
print(f"center: {cen_a[0]:.3f} @100ns -> {cen_a[-1]:.3f} @1000ns "
      f"(shift {cen_a[-1] - cen_a[0]:+.3f} cm-1); "
      f"FWHM {w_a[0]:.2f} -> {w_a[-1]:.2f}")

# ---- fig: power linearity ---------------------------------------------------
fig, ax = plt.subplots(figsize=(5.2, 3.7))
pf = np.array([0, 6.4])
ax.plot(pf, k_lin * pf, color=BLUE, lw=1.5, label="linear fit through origin")
ax.plot(P_a, area_a, "o", ms=5.5, color=INK, mfc=ORANGE, mew=0.8,
        label="measured (100–1000 ns)")
for t, p, a in [(100, P_a[0], area_a[0]), (500, P_a[4], area_a[4]),
                (1000, P_a[-1], area_a[-1])]:
    ax.annotate(f"{t:.0f} ns", (p, a), textcoords="offset points",
                xytext=(6, -9), fontsize=8, color=MUTED)
ax.set_xlabel("average optical power (mW)")
ax.set_ylabel(r"R15 line area (mV$\cdot$cm$^{-1}$)")
ax.set_xlim(0, 6.5)
ax.set_ylim(0, None)
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(HERE / f"fig-power-linearity.{ext}",
                dpi=300, bbox_inches="tight")
print("wrote fig-power-linearity.(png|pdf)")

# ---- fig: pulse characterization -------------------------------------------
fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(5.2, 6.2), sharex=True,
                                 gridspec_kw={"hspace": 0.12})
a1.plot(tau_a, ppeak, "o-", ms=4.5, lw=0.9, color=INK, mfc=ORANGE, mew=0.8)
a1.set_ylabel("peak power (mW)")
a1.set_ylim(0, 720)
a2.plot(tau_a, cen_a - cen_a[4], "o-", ms=4.5, lw=0.9, color=INK,
        mfc=ORANGE, mew=0.8)
a2.axhline(0, color=MUTED, lw=0.7, ls=":")
a2.set_ylabel(r"line-centre shift (cm$^{-1}$)")
a3.plot(tau_a, w_a, "o-", ms=4.5, lw=0.9, color=INK, mfc=ORANGE, mew=0.8)
a3.set_ylabel(r"effective FWHM (cm$^{-1}$)")
a3.set_xlabel("pulse width (ns)")
a3.set_xlim(50, 1050)
fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(HERE / f"fig-pulse-characterization.{ext}", dpi=300,
                bbox_inches="tight")
print("wrote fig-pulse-characterization.(png|pdf)")
