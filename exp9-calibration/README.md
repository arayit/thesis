# Exp 9 — concentration calibration at R15 (3 Aug 2026)

Two-MFC dilution at constant total 10 sccm, 205 Torr flow. Ladder
100/80/60/40/25/10/5/0 ppm + return-to-100; per step 60 s at the peak
(nominal 1298.1) and at the valley (1297.7); signal = peak - valley.

**Result:** k = 0.20 mV/ppm; blank at zero; return +5.1%. Sensor-noise
projected LOD 0.6 ppm (1 sigma, 60 s). The 5-60 ppm steps read low vs
nominal — attributed to mix-MFC underdelivery near its turndown floor
(descending-ladder settling would bias the other way); redo with MFC
readbacks planned.

Run: `python3 analysis.py` -> `exp9-calibration.png`;
clean version: `fig-calibration.png`
