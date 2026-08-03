# Exp 4 — pure-N₂ wavelength scan 1295–1300 cm⁻¹ (28 Jul 2026, 15:06–15:50)

**Files:** `exp4-scan/qepas_20260728_*_N2_*.csv` — 51 points, 0.1 cm⁻¹ steps,
one 30 s logger file per set point (10 Hz, TC 3 s, sens 200 mV). Sealed
chamber at 600 Torr (PCD dead-end regulation, 10 sccm supply-side MFC),
pure N₂ 6.0, 500 ns, ~3.2–3.4 mW, transmission ≈ 0.86 ≈ theoretical.
Operator notes in `exp4-scan/exp-details.txt`.

**Analysis:** `analysis/exp4_scan_fit.py` → `figures/exp4-scan-fit.(png|pdf)`.
Per point: median R over t > 10 s (TC settling dropped), DAQ zero
(−0.15 mV) subtracted, normalized to mean laser power. Fit model:
HITRAN-simulated H₂O + N₂O absorption (600 Torr Lorentzian broadening,
Gaussian laser lineshape) + linear baseline; instrument offset δ and
laser FWHM grid-searched, amplitudes by linear least squares.

## Result: the anomalous background IS water — confirmed

| Model | R² |
|---|---|
| **H₂O + N₂O + baseline** | **0.9922** |
| H₂O only + baseline | 0.9919 |
| N₂O only + baseline | 0.0385 |

The spectrum is a single blended peak complex (max 59 mV at nominal
1296.9) with a resolved satellite at nominal ~1297.4 and a flat ~10.5 mV
floor. **All three water features appear at the right positions with the
right relative intensities**: the 1296.49 doublet (left shoulder), the
1296.709 hot line (main peak), and the weak 1297.18 pair (satellite —
visible exactly where predicted). The six equal-strength N₂O R-branch
pickets in this window (R12–R17) are silent: an N₂O-only model explains
4% of the variance. Residual rms 1.05 mV on a 10–59 mV spectrum.

### Fitted parameters

- **Instrument offset δ = −0.23 cm⁻¹** (actual = nominal − 0.23).
  July-3 session had δ = +0.35: the EC-QCL set-point offset is
  *per-session* (spec ±0.5) and must be measured each session — a scan
  like this one calibrates it for free.
- **Effective laser linewidth FWHM = 0.26 cm⁻¹** — first direct
  measurement; confirms the 0.2–0.3 cm⁻¹ inference from the July-3 scan
  contrast.
- **Water amount ≈ 1.0 × saturation at 25 °C** (4.1%, ~25 Torr partial
  pressure), anchored to the historical 100-ppm-N₂O ≈ 45 mV responsivity.
  The anchor is from a different day/alignment, so read this as
  0.8–1.3× saturation — i.e. **the sealed chamber is at or near water
  saturation**, exactly what a condensed liquid reservoir produces.
- Residual N₂O component: 1.5 ppm equivalent — at the level where it
  trades against baseline undulation; treat as "≲ a few ppm".
- Baseline 10.5 mV, spectrally flat (−0.15 mV/cm⁻¹ tilt). Higher than
  the 21-Jul post-purge ~3 mV and 27-Jul ~6 mV — the known slowly
  drifting optical background, within its documented 0–13 mV range.

### Day-to-day reproducibility

Yesterday's three sealed-fill probe points (nominal 1296.7 / 1297.1 /
1297.6 → 42 / 27 / 12 mV) match today's scan at the same nominals
(45.6 / 29.2 / 12.1 mV): the water background is stable and reproducible
between sessions, as a saturated-vapor equilibrium should be.

### Residual structure (honest accounting)

- ±2–3 mV systematic wiggle across the main peak: lineshape mismatch
  (true laser lineshape is not exactly Gaussian; H₂O line-strength
  ratios shift with gas temperature). Does not affect the identification.
- Slow ±1.5 mV undulation elsewhere (bumps near 1295.6, 1297.9, 1298.9,
  1300.0): scale and ~10-min timescale of the documented optical
  background drift. No end-of-scan anchor point was recorded, so drift
  cannot be closed out exactly — next scan: re-measure the first point
  at the end.
- The par file covers 1295–1300 only; the outermost points lack
  out-of-window wing contributions.

### Caveats

- Power-meter wavelength not updated for points below 1296.5
  (≤0.1 mW ≈ 3% error there; operator note).
- `Gas.concentration = 100,%` and `adm_pressure = 600 torr` metadata:
  pressure is the PCD setpoint of a sealed volume — valid in this
  closed-chamber mode.

## Consequences

1. **The week-long anomaly is closed.** Condensed-water reservoir →
   saturated vapor in every sealed fill → 50 mV-scale absorption on the
   1296.5–1296.7 H₂O hot lines. The operator's original suspicion is
   confirmed quantitatively.
2. **R14 (actual 1297.05) is unusable while the system is wet** — it
   sits on the water complex's flank (~20 mV of water there today).
3. **R15 (actual 1297.83 = nominal 1298.06 at today's δ) is clean**:
   measured background there is ~1 mV over the floor; modeled water
   contribution ≲ 0.5 mV — the ~350× clearance of the reference figure,
   now verified experimentally. N₂O detection proceeds at R15.
4. Drying (long warm purge, capped pipes) is still worthwhile — the
   reservoir will otherwise keep re-saturating sealed fills — but it is
   no longer a blocker for N₂O detection at R15.
