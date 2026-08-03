#!/usr/bin/env python3
"""Clean thesis-grade versions of the 3 Aug 2026 figures.

Style: no in-figure titles (captions live in the thesis text), no
annotation boxes, actual wavenumber axis (per-session set-point offset
delta applied), minimal legends, no grids. Detailed working versions
remain in figures/ alongside.

Outputs (figures/thesis/):
  fig-r15-line     exp6 fine scan + HITRAN fit
  fig-comb         exp7 blank vs exp8 100 ppm, R12-R17 labeled
  fig-calibration  exp9 ladder + linear fit
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parent.parent
DAY = ROOT / "experimental" / "daq" / "2026-08-03"
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1111-2000_hitran.par"  # includes R11
OUT = ROOT / "figures" / "thesis"
OUT.mkdir(exist_ok=True)

T_K = 294.0
C_N2O_REF = 100e-6
DAQ_OFFSET_MV = -0.15

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"

plt.rcParams.update({
    "font.size": 9.5, "axes.labelsize": 10, "legend.fontsize": 9,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
    "axes.spines.top": False, "axes.spines.right": False,
})


def read_point(path):
    wl = power = conc = None
    t, r = [], []
    for line in open(path):
        if line.startswith("#"):
            if "Laser.wavelength" in line:
                wl = float(line.split(",")[1])
            elif "Laser.power" in line:
                power = float(line.split(",")[1])
            elif "Gas.concentration" in line:
                v = line.split(",")[1].strip()
                conc = float(v) if v else 0.0
            continue
        if line.startswith("iso_time"):
            continue
        p = line.strip().split(",")
        if len(p) >= 10:
            t.append(float(p[2]))
            r.append(float(p[9]) * 1000.0)
    t, r = np.array(t), np.array(r)
    core = r[t > 10.0]
    return wl, np.median(core), core.std(), power, conc


lines = {1: [], 4: []}
for l in open(PAR):
    if len(l) < 120:
        continue
    mol = int(l[0:2])
    if mol in lines:
        nu0 = float(l[3:15])
        if 1290.0 < nu0 < 1305.0:
            lines[mol].append((nu0, float(l[15:25]), float(l[35:40])))

grid = np.arange(1293.5, 1301.5, 0.002)


def alpha(mol, conc, p_torr):
    n_tot = (p_torr / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6
    a = np.zeros_like(grid)
    for nu0, S, g_air in lines[mol]:
        g = max(g_air * (p_torr / 760.0), 0.006)
        a += S * conc * n_tot * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
    return a


def convolved(a, w):
    sig = w / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a, k / k.sum(), mode="same")


def savefig(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    print(f"wrote figures/thesis/{name}.(png|pdf)")


# ---- Fig 1: exp6 R15 line ---------------------------------------------------
pts = sorted(read_point(f) for f in (DAY / "exp6-scan").glob("qepas_*.csv"))
pts = [p for p in pts if p[0] > 1297.0]
nu = np.array([p[0] for p in pts])
r = np.array([p[1] for p in pts]) - DAQ_OFFSET_MV
rs = np.array([p[2] for p in pts])

a_n = alpha(4, C_N2O_REF, 205.0)
best = None
for w in np.arange(0.14, 0.40, 0.01):
    cn = convolved(a_n, w)
    for d in np.arange(-0.40, 0.01, 0.005):
        mn = np.interp(nu + d, grid, cn)
        A = np.column_stack([np.ones_like(nu), mn])
        coef, *_ = np.linalg.lstsq(A, r, rcond=None)
        sse = ((r - A @ coef) ** 2).sum()
        if best is None or sse < best[0]:
            best = (sse, d, w, coef)
_, d6, w6, (c06, B6) = best

fig, ax = plt.subplots(figsize=(5.6, 3.4))
nu_c = np.arange(1297.2, 1298.5, 0.005)
ax.plot(nu_c, c06 + B6 * np.interp(nu_c, grid, convolved(a_n, w6)),
        color=BLUE, lw=1.6, label="HITRAN model")
ax.errorbar(nu + d6, r, yerr=rs, fmt="o", ms=4.5, color=INK, mfc=ORANGE,
            mew=0.8, elinewidth=0.9, capsize=2, label="measured")
ax.set_xlabel(r"wavenumber (cm$^{-1}$)")
ax.set_ylabel("QEPAS signal (mV)")
ax.set_xlim(1297.25, 1298.4)
ax.set_ylim(0, 33)
ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.annotate("R15", (1297.8314, 31), ha="center", fontsize=9, color=MUTED)
ax.legend(frameon=False, loc="upper right")
savefig(fig, "fig-r15-line")

# ---- Fig 2: exp7/exp8 comb --------------------------------------------------
def load_scan(folder, tag):
    pts = sorted(read_point(f) for f in folder.glob(f"qepas_*.csv"))
    seen, out = set(), []
    for p in pts:
        if p[0] in seen:
            continue                      # drop closing anchor duplicate
        seen.add(p[0])
        out.append(p)
    nu = np.array([p[0] for p in out])
    r = np.array([p[1] for p in out]) - DAQ_OFFSET_MV
    pw = np.array([p[3] for p in out])
    return nu, r * (pw.mean() / pw)


nu7, r7 = load_scan(DAY / "exp7-scan", "N2")
nu8, r8 = load_scan(DAY / "exp8-scan", "N2O")

a_w = alpha(1, 23.76 / 205.0, 205.0)
best = None
for w in np.arange(0.16, 0.32, 0.01):
    cw, cn = convolved(a_w, w), convolved(a_n, w)
    for d in np.arange(-0.35, -0.10, 0.005):
        mw = np.interp(nu8 + d, grid, cw)
        mn = np.interp(nu8 + d, grid, cn)
        A = np.column_stack([np.ones_like(nu8), nu8 - nu8.mean(), mw, mn])
        coef, *_ = np.linalg.lstsq(A, r8, rcond=None)
        sse = ((r8 - A @ coef) ** 2).sum()
        if best is None or sse < best[0]:
            best = (sse, d, w, coef)
_, d78, w78, (c078, c178, Bw78, Bn78) = best

fig, ax = plt.subplots(figsize=(6.6, 3.6))
nu_c = np.arange(1294.7, 1299.9, 0.005)
fit_c = (c078 + c178 * (nu_c - d78 - nu8.mean())
         + Bw78 * np.interp(nu_c, grid, convolved(a_w, w78))
         + Bn78 * np.interp(nu_c, grid, convolved(a_n, w78)))
ax.plot(nu_c, fit_c, color=BLUE, lw=1.2, alpha=0.85, label="HITRAN model")
ax.plot(nu7 + d78, r7, "s", ms=3.2, color=MUTED, mfc="white", mew=0.8,
        label="pure N$_2$")
ax.plot(nu8 + d78, r8, "o", ms=4.0, color=INK, mfc=ORANGE, mew=0.7,
        label="100 ppm N$_2$O")
for j, nu0 in zip(range(11, 18), [1294.6845, 1295.4766, 1296.2651, 1297.0501,
                                  1297.8314, 1298.6093, 1299.3835]):
    if nu0 > 1294.75:
        ax.annotate(f"R{j}", (nu0, 29.5), ha="center", fontsize=8, color=MUTED)
ax.set_xlabel(r"wavenumber (cm$^{-1}$)")
ax.set_ylabel("QEPAS signal (mV)")
ax.set_xlim(1294.7, 1299.9)
ax.set_ylim(0, 32)
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
ax.legend(frameon=False, loc="lower center", ncols=3,
          columnspacing=1.2, handletextpad=0.5)
savefig(fig, "fig-comb")

# ---- Fig 3: exp9 calibration ------------------------------------------------
pts = sorted((read_point(f), f.name)
             for f in (DAY / "exp9-calibration").glob("qepas_*.csv"))
pts = [p[0] for p in pts]
# chronological pairing: files sorted by name = time
raw = sorted(
    (read_point(f) for f in (DAY / "exp9-calibration").glob("qepas_*.csv")),
    key=lambda p: 0)
files = sorted((DAY / "exp9-calibration").glob("qepas_*.csv"))
seq = [read_point(f) for f in files]
steps = []
for i in range(0, len(seq), 2):
    wl1, m1, s1, _, c1 = seq[i]
    wl2, m2, s2, _, c2 = seq[i + 1]
    steps.append((c1, m1 - m2, float(np.hypot(s1, s2))))
C = np.array([s[0] for s in steps[:8]])
D = np.array([s[1] for s in steps[:8]])
E = np.array([s[2] for s in steps[:8]])
cr, dr, er = steps[8]
A = np.column_stack([C, np.ones_like(C)])
(k_all, b_all), *_ = np.linalg.lstsq(A, D, rcond=None)

fig, ax = plt.subplots(figsize=(5.0, 3.6))
cf = np.array([-2, 105])
ax.plot(cf, k_all * cf + b_all, color=BLUE, lw=1.4,
        label=f"linear fit, {k_all:.2f} mV/ppm")
ax.errorbar(C, D, yerr=E, fmt="o", ms=5, color=INK, mfc=ORANGE, mew=0.8,
            elinewidth=0.9, capsize=2, label="measured")
ax.plot([cr], [dr], "D", ms=6, color=INK, mfc="white", mew=1.2,
        label="repeat (100 ppm)")
ax.set_xlabel(r"N$_2$O concentration (ppm)")
ax.set_ylabel(r"QEPAS signal (mV)")
ax.set_xlim(-4, 108)
ax.set_ylim(-1.5, 23)
ax.legend(frameon=False, loc="upper left")
savefig(fig, "fig-calibration")
