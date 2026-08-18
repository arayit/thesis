#!/usr/bin/env python3
"""Relative line-intensity analysis of the exp8 comb (3 Aug 2026).

Each picket R12-R17 in the difference spectrum (exp8 - exp7) is fitted
locally (single convolved line + flat offset, global delta and laser
FWHM fixed from the comb fit) to extract its amplitude free of grid-
sampling bias. Measured relative amplitudes are compared with the
HITRAN S(296 K) predictions, and a rotational temperature is estimated
from the J-dependence of the Boltzmann populations.

Output: figures/exp8-line-intensities.(png|pdf) + table on stdout.
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DAY = None
PAR = ROOT / "hitran" / "h2o_n2o_1111-2000_hitran.par"

P_TORR = 205.0
DAQ_OFFSET_MV = -0.15
DELTA, W_FWHM = -0.23, 0.20            # global comb-fit values
B_ROT = 0.4190                          # N2O ground-state B (cm-1)
HCK = 1.4388                            # hc/k (cm K)

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"

plt.rcParams.update({
    "font.size": 9.5, "axes.labelsize": 10, "legend.fontsize": 9,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
    "axes.spines.top": False, "axes.spines.right": False,
})


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


def load_scan(folder):
    pts = sorted(read_point(f) for f in folder.glob("qepas_*.csv"))
    seen, out = set(), []
    for p in pts:
        if p[0] in seen:
            continue
        seen.add(p[0])
        out.append(p)
    nu = np.array([p[0] for p in out])
    r = np.array([p[1] for p in out]) - DAQ_OFFSET_MV
    s = np.array([p[2] for p in out])
    pw = np.array([p[3] for p in out])
    return nu, r * (pw.mean() / pw), s


nu7, r7, s7 = load_scan(ROOT / "exp7-blank-scan" / "data")
nu8, r8, s8 = load_scan(HERE / "data")
diff = r8 - r7
sd = np.sqrt(s7 ** 2 + s8 ** 2)

# R12-R17 lines from HITRAN (position, S, gamma_air, J)
COMB = {12: 1295.4766, 13: 1296.2651, 14: 1297.0501,
        15: 1297.8314, 16: 1298.6093, 17: 1299.3835}
S_HIT, G_AIR = {}, {}
for l in open(PAR):
    if len(l) < 120:
        continue
    if int(l[0:2]) == 4:
        nu0, S = float(l[3:15]), float(l[15:25])
        for j, c in COMB.items():
            if abs(nu0 - c) < 2e-3 and S > S_HIT.get(j, 0.0):
                S_HIT[j], G_AIR[j] = S, float(l[35:40])   # strongest match

grid = np.arange(1293.5, 1301.5, 0.002)
sig = W_FWHM / 2.3548 / 0.002
n = int(6 * sig) + 1
kern = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
kern /= kern.sum()


def single_line(j):
    g = max(G_AIR[j] * (P_TORR / 760.0), 0.006)
    a = g / (np.pi * ((grid - COMB[j]) ** 2 + g ** 2))   # unit-area profile
    return np.convolve(a, kern, mode="same")


print(f"{'line':>5} {'S_HITRAN':>10} {'meas amp':>9} {'meas rel':>9} "
      f"{'HITRAN rel':>10} {'dev':>6}")
amps, errs = {}, {}
for j in COMB:
    m = np.abs(nu8 - (COMB[j] - DELTA)) <= 0.35
    if m.sum() < 5:
        continue
    prof = np.interp(nu8[m] + DELTA, grid, single_line(j))
    A = np.column_stack([np.ones(m.sum()), prof])
    coef, *_ = np.linalg.lstsq(A, diff[m], rcond=None)
    res = diff[m] - A @ coef
    cov = (res ** 2).sum() / (m.sum() - 2) * np.linalg.inv(A.T @ A)
    amps[j], errs[j] = coef[1], np.sqrt(cov[1, 1])

ref = 15
meas_rel = {j: amps[j] / amps[ref] for j in amps}
err_rel = {j: errs[j] / amps[ref] for j in amps}
hit_rel = {j: S_HIT[j] / S_HIT[ref] for j in amps}
for j in sorted(amps):
    dev = 100 * (meas_rel[j] / hit_rel[j] - 1)
    print(f"  R{j:<3d} {S_HIT[j]:10.3e} {amps[j]:9.3f} {meas_rel[j]:9.3f} "
          f"{hit_rel[j]:10.3f} {dev:+5.1f}%")

# rotational temperature from the J-dependence
def rel_S(T):
    # S(J,T)/S(15,T): population ratio x (transition-moment J-factors cancel
    # to first order within the narrow J range; E'' = B J(J+1))
    out = {}
    e15 = B_ROT * ref * (ref + 1)
    for j in amps:
        e = B_ROT * j * (j + 1)
        s296 = S_HIT[j] / S_HIT[ref]
        # remove the 296 K Boltzmann factor, apply T's
        corr = np.exp(-HCK * (e - e15) / T) / np.exp(-HCK * (e - e15) / 296.0)
        out[j] = s296 * corr
    return out

T_LINES = [j for j in amps if j not in (ref, 14, 16)]   # R14/R16 anomalous
Ts = np.arange(200.0, 420.0, 1.0)
chi = []
for T in Ts:
    rs = rel_S(T)
    chi.append(sum(((meas_rel[j] - rs[j]) / max(err_rel[j], 0.005)) ** 2
                   for j in T_LINES))
chi = np.array(chi)
Tbest = Ts[np.argmin(chi)]
in1 = Ts[chi < chi.min() + 1]
print(f"\nrotational-T fit (R12/13/17 vs R15 only): best {Tbest:.0f} K, "
      f"68% range {in1[0]:.0f}-{in1[-1]:.0f} K — J-lever too weak after "
      f"excluding R14/R16; T effectively unconstrained, table is the result")
rms = np.sqrt(np.mean([(meas_rel[j] / hit_rel[j] - 1) ** 2
                       for j in amps if j != ref])) * 100
print(f"rms deviation from HITRAN relative intensities: {rms:.1f}%")

fig, ax = plt.subplots(figsize=(5.0, 3.6))
ax.plot([0.80, 1.05], [0.80, 1.05], color=MUTED, lw=0.9, ls="--",
        label="1:1")
for j in sorted(amps):
    ax.errorbar(hit_rel[j], meas_rel[j], yerr=err_rel[j], fmt="o", ms=5.5,
                color=INK, mfc=ORANGE, mew=0.8, elinewidth=0.9, capsize=2)
    ax.annotate(f"R{j}", (hit_rel[j], meas_rel[j]),
                textcoords="offset points", xytext=(6, -3), fontsize=8,
                color=MUTED)
ax.set_xlabel("HITRAN relative intensity (R15 = 1)")
ax.set_ylabel("measured relative amplitude")
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
out = HERE / "exp8-line-intensities"
fig.savefig(f"{out}.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{out}.pdf", bbox_inches="tight")
print(f"wrote {out}.png/.pdf")
