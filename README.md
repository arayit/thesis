# QEPAS N2O sensor — experiment record

Pulsed-QCL (EC-QCL, 7.7 um) quartz-enhanced photoacoustic N2O sensor;
QTF f0 = 12458.8 Hz, 1f-AM detection. Each folder: raw logger CSVs
(`data/`), the analysis script, and the resulting figures. Scripts run
in place (`python3 analysis.py`); HITRAN line lists in `hitran/`.
Set-point offset convention: actual = nominal + delta.

| Exp | Date | What | Key result |
|---|---|---|---|
| exp4 | 28 Jul | pure-N2 scan 1295-1300, sealed 600 Torr | anomalous background = water (R2=0.992); delta=-0.23, laser FWHM 0.26 cm-1 |
| exp5 | 31 Jul | same scan, "100 ppm N2O" sealed fills | no N2O (-1.5+-1.1 ppm): sealed fills do not deliver gas to the cell |
| exp6 | 3 Aug | R15 fine scan, constant flow 205 Torr | first N2O detection since Dec 2025; gas-switch control 26->9 mV |
| exp7 | 3 Aug | pure-N2 blank, full window, flow | flow-mode background; lab 21 C / 75% RH |
| exp8 | 3 Aug | 100 ppm full window, flow | complete R12-R17 comb at HITRAN positions |
| exp9 | 3 Aug | concentration ladder at R15 | k = 0.20 mV/ppm; projected LOD 0.6 ppm (1 sigma, 60 s) |
| exp10 | 17 Aug | pulse-width series 100-1000 ns | signal proportional to power (4% rms); QCL rollover -27%; chirp map |
