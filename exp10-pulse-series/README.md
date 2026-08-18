# Exp 10 — pulse-width (power) series (17 Aug 2026)

10 pulse widths 100-1000 ns at fixed rep rate = f0; per width a 6-7
point mini-profile across R15; 100 ppm N2O, constant flow, 199 Torr.
Per-width profile fits give amplitude, line centre and effective width.

**Results:** (1) R15 line area proportional to measured average power
(4.1% rms over 7.3x) — measured basis for power normalization/NNEA;
(2) QCL thermal rollover: P_peak 665 -> 484 mW (-27%);
(3) chirp map: line centre shifts +0.075 cm-1 (nominal) from 100 to
1000 ns — the set-point offset delta is pulse-width dependent; at the
500 ns operating point delta = -0.215, unchanged for three weeks.

Run: `python3 analysis.py` -> `fig-power-linearity.png`,
`fig-pulse-characterization.png`
