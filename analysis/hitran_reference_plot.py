#!/usr/bin/env python3
"""Reference figure: N2O vs H2O absorption around the QEPAS operating lines.

Reads the HITRAN subset (data/hitran/h2o_n2o_1295-1300_hitran.par, .par format)
and renders two panels:
  (a) stick spectrum of line intensities S(296 K), log scale;
  (b) simulated absorption coefficient at lab conditions -- 600 Torr, 298 K,
      100 ppm N2O vs water-saturated air (3.96% at 25 C), Lorentzian profiles
      with air broadening. This is the "what the sensor sees" panel that
      motivates the R15 operating-line choice.

Output: figures/hitran-n2o-h2o-reference.(png|pdf)
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1295-1300_hitran.par"

# Lab conditions
P_TORR, T_K = 600.0, 298.0
C_N2O = 100e-6                      # 100 ppm
C_H2O = 23.76 / P_TORR              # saturation at 25 C -> 3.96%
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6  # molec/cm^3

BLUE, ORANGE = "#2a78d6", "#eb6834"     # categorical slots 1-2 (validated)
INK, MUTED = "#1a1a19", "#6b6a63"

N2O_MARKS = {"R13": 1296.2651, "R14": 1297.0501, "R15": 1297.8314, "R16": 1298.6093}


def load(par_path):
    lines = {1: [], 4: []}
    for l in open(par_path):
        if len(l) < 120:
            continue
        mol = int(l[0:2])
        if mol in lines:
            lines[mol].append((float(l[3:15]), float(l[15:25]), float(l[35:40])))
    return {m: np.array(v) for m, v in lines.items()}


def alpha(grid, lines, conc):
    a = np.zeros_like(grid)
    for nu0, S, g_air in lines:
        g = max(g_air, 0.02) * (P_TORR / 760.0)          # cm-1 HWHM at P
        a += S * conc * N_TOT * g / (np.pi * ((grid - nu0) ** 2 + g ** 2))
    return a


data = load(PAR)
grid = np.arange(1295.0, 1300.0, 0.002)
a_n2o = alpha(grid, data[4], C_N2O)
a_h2o = alpha(grid, data[1], C_H2O)

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(9.5, 6.4), sharex=True, gridspec_kw={"height_ratios": [1, 1.35]}
)
fig.patch.set_facecolor("white")

# ---- (a) stick spectrum -----------------------------------------------------
for mol, col, lab in ((4, BLUE, r"N$_2$O"), (1, ORANGE, r"H$_2$O")):
    nu, S = data[mol][:, 0], data[mol][:, 1]
    ax1.vlines(nu, 1e-25, S, color=col, lw=1.4 if mol == 1 else 1.0, alpha=0.9, label=lab)
ax1.set_yscale("log")
ax1.set_ylim(1e-25, 8e-19)
ax1.set_ylabel(r"line intensity $S$ (cm/molec)")
ax1.legend(loc="upper right", frameon=False, fontsize=9)
for name, nu in N2O_MARKS.items():
    ax1.annotate(name, (nu, 2.4e-19), ha="center", fontsize=8, color=INK)
ax1.annotate("H$_2$O hot lines", (1296.60, 1.2e-21), ha="center", fontsize=8, color=ORANGE)
ax1.set_title(
    "HITRAN 2020: N$_2$O $\\nu_1$ R-branch vs H$_2$O around the QEPAS operating region",
    fontsize=10.5, color=INK,
)

# ---- (b) simulated absorption at lab conditions -----------------------------
ax2.plot(grid, a_n2o, color=BLUE, lw=1.6, label=r"100 ppm N$_2$O")
ax2.plot(grid, a_h2o, color=ORANGE, lw=1.6, label=r"H$_2$O, saturated (4.0% @ 25$^\circ$C)")
ax2.set_yscale("log")
ax2.set_ylim(1e-8, 2e-2)
ax2.set_xlim(1295.0, 1300.0)
ax2.set_ylabel(r"absorption coeff. $\alpha$ (cm$^{-1}$)")
ax2.set_xlabel(r"wavenumber (cm$^{-1}$)")
ax2.legend(loc="upper right", frameon=False, fontsize=9)

from matplotlib.ticker import MultipleLocator

for ax in (ax1, ax2):
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_formatter("{x:.1f}")
    ax.grid(True, axis="x", which="minor", alpha=0.10, lw=0.4)
    ax.grid(True, axis="both", which="major", alpha=0.18, lw=0.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8.5, color=MUTED)

fig.tight_layout(h_pad=1.2)
out = ROOT / "figures" / "hitran-n2o-h2o-reference"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"wrote {out}.png/.pdf")
print(f"peak alpha N2O(R14) = {a_n2o.max():.2e} cm-1 ; H2O(1296.71) = {a_h2o.max():.2e} cm-1")
