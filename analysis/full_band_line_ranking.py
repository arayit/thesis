#!/usr/bin/env python3
"""Rank every strong N2O line 1111-2000 cm-1 against the saturated-water
background, at the conditions fitted from the 28-Jul scan.

Input: data/hitran/h2o_n2o_1111-2000_hitran.par (H2O + N2O, fetched
31 Jul 2026). Conditions: 600 Torr, 298 K, laser FWHM 0.26 cm-1 (fitted),
H2O at the fitted 24.7 Torr partial pressure, N2O at 100 ppm reference.
Signals in mV via the historical responsivity anchor (100 ppm N2O ~ 45 mV
at R14, ~3.2 mW).

Output (stdout): per-line table [nu, S, 100ppm-N2O signal, water
background, ratio] for all N2O lines with S > 1e-19, the best clean set
points file-wide, and the band-centre zero-gap reference survey.
Result: R15 (1297.8314) confirmed as operating line; gap reference at
actual ~1285.17.
"""
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
PAR = ROOT / "data" / "hitran" / "h2o_n2o_1111-2000_hitran.par"

P_TORR, T_K = 600.0, 298.0
C_N2O = 100e-6                 # reference concentration
C_H2O = 24.7 / P_TORR          # fitted 28-Jul water partial pressure
W_FWHM = 0.26                  # fitted laser lineshape FWHM
B_RESP = 51788.0               # mV per cm^-1 alpha (R14 responsivity anchor)
N_TOT = (P_TORR / 760.0) * 101325 / (1.380649e-23 * T_K) * 1e-6

lines = {1: [], 4: []}
for l in open(PAR):
    if len(l) < 120:
        continue
    mol = int(l[0:2])
    if mol in lines:
        lines[mol].append((float(l[3:15]), float(l[15:25]), float(l[35:40])))
numin = min(x[0] for v in lines.values() for x in v)
numax = max(x[0] for v in lines.values() for x in v)
print(f"range {numin:.1f}-{numax:.1f}; H2O {len(lines[1])} lines, "
      f"N2O {len(lines[4])} lines")

grid = np.arange(numin - 2, numax + 2, 0.002)


def alpha(mol, conc):
    a = np.zeros_like(grid)
    for nu0, S, g_air in lines[mol]:
        g = max(g_air, 0.02) * (P_TORR / 760.0)
        m = np.abs(grid - nu0) < 6.0            # truncate far wings
        a[m] += S * conc * N_TOT * g / (np.pi * ((grid[m] - nu0) ** 2 + g ** 2))
    return a


def convolved(a):
    sig = W_FWHM / 2.3548 / 0.002
    n = int(6 * sig) + 1
    k = np.exp(-0.5 * (np.arange(-n, n + 1) / sig) ** 2)
    return np.convolve(a, k / k.sum(), mode="same")


cw, cn = convolved(alpha(1, C_H2O)), convolved(alpha(4, C_N2O))

print(f"\nN2O lines with S > 1e-19 (the nu1 P/R comb):")
print(f"{'nu':>10} {'S':>10} {'N2O mV':>8} {'H2O mV':>8} {'N2O/H2O':>9}")
for nu0, S, g in sorted(x for x in lines[4] if x[1] > 1.0e-19):
    sn = np.interp(nu0, grid, cn) * B_RESP
    sw = np.interp(nu0, grid, cw) * B_RESP
    print(f"{nu0:10.4f} {S:10.3e} {sn:8.1f} {sw:8.2f} {sn / max(sw, 1e-9):9.0f}")

print("\nBest set points file-wide (N2O signal max, water < 0.5 mV):")
picked = []
for i in np.argsort(-(cn * (cw * B_RESP < 0.5))):
    if all(abs(grid[i] - p) > 0.5 for p in picked):
        picked.append(grid[i])
    if len(picked) >= 10:
        break
for p in sorted(picked):
    print(f"  {p:9.3f}  N2O {np.interp(p, grid, cn) * B_RESP:6.1f} mV   "
          f"H2O {np.interp(p, grid, cw) * B_RESP:5.2f} mV")

print("\nBand-centre zero-gap reference (total 100ppm-N2O + sat-H2O bkg):")
for x in np.arange(1284.9, 1285.55, 0.1):
    tot = (np.interp(x, grid, cn) + np.interp(x, grid, cw)) * B_RESP
    print(f"  {x:.1f}: {tot:5.2f} mV")
