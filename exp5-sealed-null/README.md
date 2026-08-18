# Exp 5 — sealed-fill counterpart scan (31 Jul 2026)

Same 51-point grid as exp4, chamber filled to 600 Torr from the 100 ppm
N2O cylinder (evacuate-refill, sealed). A quantitative prediction of
the expected comb was committed before the measurement
(`exp5-scan-prediction.png`).

**Result:** spectrum identical to exp4; comb-template correlation gives
-1.5 +- 1.1 ppm N2O (<= 3 ppm at 3 sigma). Instrument state reproduced
exp4 exactly (delta, FWHM, water). Conclusion (established with exp6):
sealed fills did not deliver gas to the acoustic cell; flow does.

Run: `python3 analysis.py` -> `exp5-vs-exp4.png` (needs ../exp4-water-scan/data)
