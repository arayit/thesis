# Exp 6 — first N2O detection (3 Aug 2026)

R15 fine scan (nominal 1297.5-1298.5, 0.1 steps) with 100 ppm N2O in
constant flow at 205 Torr (needle valve at ADM output).

**Result:** clean absorption line at R15 (1297.8314 cm-1): position
(delta = -0.22), width (laser-limited 0.24 cm-1) and amplitude all
match; supply switch N2O -> N2 dropped the signal 26 -> 9 mV.
First detection since December 2025.

Run: `python3 analysis.py` -> `exp6-r15-line.png` (needs ../exp5-sealed-null/data);
clean version: `fig-r15-line.png`
