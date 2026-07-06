# analysis/

Fit and plotting scripts so every thesis figure regenerates from the raw data
in `experimental/`. Scripts to be added here (currently live in claude.ai
sessions / outside the repo):

- QTF Lorentzian fit (ADM resonance sweeps, 100 & 50 mV drive) → f₀, Q
- Power-linearity fit (background vs average power, R² = 0.989)
- Wavelength-scan plot (the 1296.7 cm⁻¹ line-location scan)
- `beam_propagation.py` (LightPipes; add the decenter scan + measured input
  beam size once the QCL→OAP distance is measured)

Convention: each script reads from `experimental/`, writes a PDF into
`figures/`, and is runnable headless (no notebook state).
