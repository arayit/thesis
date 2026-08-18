# Exp 10 — pulse-width (power) series on R15 (17 Aug 2026, 15:46–17:50)

**Files:** `exp10-pulse-series/` — 10 pulse widths (100–1000 ns, 100 ns
steps) at fixed rep rate 12458.8 Hz = f₀; per width a 6–7 point
mini-profile across R15 (nominal 1297.7–1298.3, 30 s/point), 100 ppm
N₂O in constant flow at 199 Torr, sens 200 mV, TC 3 s. A few grid
points missing (100 ns: 1297.9; 600 ns: 1297.8; 1000 ns: 1298.1) —
profile fits recover peak/center/width regardless.

**Analysis:** `analysis/exp10_pulse_series.py` →
`figures/thesis/fig-power-linearity` and `fig-pulse-characterization`.
Per width, the mini-profile is fitted with the HITRAN N₂O model
(199 Torr, Gaussian laser lineshape; free amplitude, offset, center,
width). The linearity test uses the fitted **line area** — invariant
to chirp-induced lineshape changes, unlike the peak height.

## Results

1. **Signal ∝ optical power confirmed**: line area = 2.22 × P_avg over
   a 7.3× power range (0.83–6.08 mW), rms deviation 4.1%. The 300–1000
   ns points sit within ±5% of the through-origin line; 100–200 ns fall
   below it (low-SNR 6-point fits; peak only 4 mV over floor at
   100 ns). This measured proportionality underpins the power
   normalization used throughout and the NNEA quotation.
2. **QCL thermal rollover measured**: P_peak = P_avg/duty falls from
   665 mW (100 ns) to 484 mW (1000 ns), −27% — textbook intra-pulse
   heating behaviour.
3. **Chirp map — the set-point offset is pulse-width dependent**: the
   fitted line centre moves +0.075 cm⁻¹ in nominal terms from 100 to
   1000 ns (laser red-shifts as the pulse lengthens), saturating above
   ~800 ns. Effective laser FWHM stays 0.23–0.27 cm⁻¹ with no strong
   trend. Consequence: **δ must always be quoted at the operating
   pulse width**; all our calibrations are at 500 ns.
4. **δ stability across two weeks**: at 500 ns the centre gives
   δ = −0.215, vs −0.22…−0.24 in all four sessions of 28 Jul–3 Aug.
   The set-point offset has been stable for three weeks (at fixed τ).
5. Peak signal at 100 ppm nearly doubles from 500 ns (27.6 mV) to
   900 ns (43 mV) — but the plateau noise grows with power too
   (0.04 → 0.10 mV), so the SNR gain is modest. 500 ns remains the
   calibrated standard operating point; a dedicated noise-vs-τ study
   would be needed before moving.

## Consequences

- Power normalization and NNEA now rest on a measured linearity, not
  an assumption.
- The chirp map explains why per-session δ checks must be done at the
  operating pulse width, and quantifies the cost of changing τ
  mid-campaign (+0.02…−0.06 cm⁻¹ apparent line shifts).
