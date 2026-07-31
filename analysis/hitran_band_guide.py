#!/usr/bin/env python3
"""Guide map: both humps of the N2O nu1 band vs saturated water, in mV.

Reads data/hitran/h2o_n2o_1111-2000_hitran.par and plots the expected
QEPAS signal (mV, via the R14 responsivity anchor) for 100 ppm N2O and
for the fitted 24.7 Torr water, both convolved with the fitted 0.26 cm-1
laser lineshape, at 600 Torr. Top axis: nominal set points at the
28-Jul session offset (delta = -0.23). Optical background (~10 mV floor)
not included.

Output: figures/hitran-band-guide.(png|pdf)
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parent.parent
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1111-2000_hitran.par"

P_TORR, T_K = 600.0, 298.0
C_N2O = 100e-6
C_H2O = 24.7 / P_TORR
W_FWHM = 0.26
B_RESP = 51788.0
DELTA = -0.23                    # actual = nominal + delta (28-Jul session)
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"

lines = {1: [], 4: []}
for l in open(PAR):
    if len(l) < 120:
        continue
    mol = int(l[0:2])
    if mol in lines:
        lines[mol].append((float(l[3:15]), float(l[15:25]), float(l[35:40])))

grid = np.arange(1252.0, 1314.0, 0.002)


def alpha(mol, conc):
    a = np.zeros_like(grid)
    for nu0, S, g_air in lines[mol]:
        if not (grid[0] - 6 < nu0 < grid[-1] + 6):
            continue
        g = max(g_air, 0.02) * (P_TORR / 760.0)
        a += S * conc * N_TOT * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
    return a


def convolved(a):
    sig = W_FWHM / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a, k / k.sum(), mode="same")


s_w = convolved(alpha(1, C_H2O)) * B_RESP
s_n = convolved(alpha(4, C_N2O)) * B_RESP

fig, ax = plt.subplots(figsize=(11.0, 4.9))
fig.patch.set_facecolor("white")

ax.fill_between(grid, s_n, color=BLUE, alpha=0.25, lw=0)
ax.plot(grid, s_n, color=BLUE, lw=1.1, label="N$_2$O 100 ppm")
ax.fill_between(grid, s_w, color=ORANGE, alpha=0.30, lw=0)
ax.plot(grid, s_w, color=ORANGE, lw=1.3, label="H$_2$O saturated (24.7 Torr)")

# verification-scan window (actual 1296.3-1300.3 = nominal 1296.5-1300.5)
ax.axvspan(1296.3, 1300.3, color=MUTED, alpha=0.08, zorder=0)
ax.annotate("verification scan\nwindow", (1298.3, 76), ha="center",
            fontsize=8, color=MUTED)

ann = dict(fontsize=8, color=INK,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.annotate("H$_2$O 1271.79\nkills P15", (1271.85, 89), (1265.5, 84),
            ha="center", **ann)
ax.annotate("H$_2$O 1296.5+1296.7\n(the 59 mV peak of the 28-Jul scan)",
            (1296.63, 48), (1288.5, 66), ha="center", **ann)
ax.annotate("R15 $\\rightarrow$ operate here\n(water < 0.3 mV)",
            (1297.83, 45.5), (1303.5, 58), ha="center", **ann)
ax.annotate("R16, R17\nfallbacks", (1299.0, 45.2), (1306.5, 40),
            ha="center", **ann)
ax.annotate("band-centre gap 1285.2\noff-line reference",
            (1285.2, 2.5), (1284.0, 22), ha="center", **ann)
ax.annotate("P branch", (1264.0, 36), fontsize=9, color=MUTED, ha="center")
ax.annotate("R branch", (1303.9, 51), fontsize=9, color=MUTED, ha="center")

# water spikes taller than the axis: print their true peak values
for x, pk in [(1260.34, 172), (1269.96, 97), (1271.79, 190),
              (1287.40, 118), (1308.18, 117)]:
    ax.annotate(f"{pk}$\\uparrow$", (x, 92.5), ha="center", fontsize=7.5,
                color=ORANGE)

ax.set_xlim(1256, 1312)
ax.set_ylim(0, 96)
ax.set_xlabel(r"actual wavenumber (cm$^{-1}$)")
ax.set_ylabel("expected QEPAS signal (mV)")
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.grid(True, axis="both", which="major", alpha=0.18, lw=0.5)
ax.grid(True, axis="x", which="minor", alpha=0.08, lw=0.4)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(labelsize=8.5, color=MUTED)
ax.legend(loc="upper right", frameon=False, fontsize=9)

sec = ax.secondary_xaxis("top", functions=(lambda x: x - DELTA,
                                           lambda x: x + DELTA))
sec.set_xlabel(r"nominal set point at this session's $\delta=-0.23$ (cm$^{-1}$)",
               fontsize=8.5, color=MUTED)
sec.tick_params(labelsize=8, color=MUTED, labelcolor=MUTED)
sec.xaxis.set_major_locator(MultipleLocator(5))

ax.set_title("Guide map: N$_2$O $\\nu_1$ band (both humps) vs saturated water — "
             "600 Torr, laser FWHM 0.26 cm$^{-1}$, ~10 mV optical background "
             "not shown", fontsize=10, color=INK)

fig.tight_layout()
out = ROOT / "figures" / "hitran-band-guide"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"wrote {out}.png/.pdf")
