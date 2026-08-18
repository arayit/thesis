# Exp 4 — pure-N2 wavelength scan (28 Jul 2026)

51 points, nominal 1295.0-1300.0, 0.1 steps, 30 s/point; sealed chamber
at 600 Torr, pure N2 6.0. Purpose: identify the anomalous 50 mV-scale
background.

**Result:** the spectrum matches the HITRAN water spectrum with
R2 = 0.992 (N2O-only model: 0.04) — the background is water at ~
saturation (internal liquid reservoir). Byproducts: set-point offset
delta = -0.23 cm-1, first direct laser linewidth measurement
(FWHM = 0.26 cm-1).

Run: `python3 analysis.py` -> `exp4-scan-fit.png`
