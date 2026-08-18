# Exp 8 — the R-branch comb (3 Aug 2026)

Same grid as exp7 with the 100 ppm mix flowing. Metadata note: the
`Gas.gas_type` field in some early files reads "N2" (logger field not
updated at session start); the flowing gas was the N2O mix throughout.

**Result:** the difference exp8 - exp7 shows six pickets R12-R17 at
0.78 cm-1 spacing, all at HITRAN positions (delta = -0.23, fourth
consecutive session). `line_intensities.py`: R12/R13/R17 relative
intensities track HITRAN within ~8%; R14/R16 read 28-36% low —
unexplained, flagged for a fine-scan check.

Run: `python3 analysis.py` -> `exp78-comb.png` (needs ../exp7-blank-scan/data);
`python3 line_intensities.py` -> `exp8-line-intensities.png`;
clean version: `fig-comb.png`
