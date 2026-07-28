# HITRAN N₂O line data (1260–1320 cm⁻¹ subset)

`n2o_1260-1320_hitran.csv` — extracted from the HITRAN .par download
(N₂O, 1111–2000 cm⁻¹, all isotopologues; fetched 20 Jul 2026). Columns:
line centre, intensity S (296 K), air/self broadening, lower-state energy,
isotopologue, band, branch/J assignment.

## Line identification (closes THESIS-PLAN A4 / CONTEXT item 4)

ν₁ fundamental (10⁰0 ← 00⁰0) R-branch of ¹⁴N₂¹⁶O around the operating
region — spacing ≈ 0.78 cm⁻¹, all S ≈ 1.7 × 10⁻¹⁹ cm/molecule:

| Line | ν (cm⁻¹) | S (cm/molec) |
|---|---|---|
| R13e | 1296.2651 | 1.693e-19 |
| **R14e** | **1297.0501** | **1.715e-19** |
| R15e | 1297.8314 | 1.721e-19 |
| R16e | 1298.6093 | 1.714e-19 |

- **The experimentally located peak (nominal set point 1296.7) = R14e at
  1297.0501 cm⁻¹.** Instrument wavenumber offset ≈ −0.35 cm⁻¹, within the
  ±0.5 spec. The step-scan "target 1297.0" was R14; the historical
  "primary line 1297.8" is R15e; the December 2025 detection at nominal
  1297.8 was therefore R15.
- The July-3 scan contrast (36 mV peak vs ~5 mV between lines, 0.78 cm⁻¹
  picket spacing) implies an **effective pulsed laser linewidth well below
  the <1 cm⁻¹ spec — roughly 0.2–0.3 cm⁻¹** — otherwise adjacent-line
  overlap would wash out the modulation.

## Methodological consequence: there is no off-line point nearby

Summing S over a ±0.4 cm⁻¹ laser envelope across 1284–1315 cm⁻¹: **no set
point below 2% of on-line absorption exists except the narrow band-centre
gap at ≈ 1285.1 cm⁻¹** (between P1 and R0). Even 1315 cm⁻¹ still sees
~24% of on-line absorption (R-branch tail + hot bands). In particular the
points used to date as "off-line" references are not:

| Nominal set point (with −0.35 offset → actual) | Nearest line | Overlap |
|---|---|---|
| 1297.6 → ~1297.95 | R15e (1297.83) | essentially on-line |
| 1298.5 → ~1298.85 | R16e (1298.61) | strong |

**Protocol change:** the off-line background reference moves to the
band-centre gap (nominal ≈ 1285.4–1285.5 given the −0.35 offset — locate
it by a mini scan 1285.0–1286.0), or background is taken by gas exchange
(pure N₂) rather than by wavelength. All prior "off-line" readings at
1297.6/1298.5 must be reinterpreted as partially on-line.

## Working hypothesis for the 20-July evening instability (to test)

Residual N₂O in the nominally pure N₂ stream (analyte-MFC leak-through
with the cylinder open — MFCs do not seal at setpoint 0 — or desorption/
dead volume) **plus** slow excursions of the actual laser frequency
(±0.2–0.3 cm⁻¹) across the R-branch picket fence would reproduce every
feature of the evening data: high wandering "N₂ baseline" at 1296.7 (R14),
smaller excursions at 1297.6 (R15 wing), the absence of a clear response
to gas switching, and zero signal with the beam blocked. Tests
(≈20 min, next session):

1. Close the N₂O **cylinder valve** (not just MFC = 0), N₂ flowing,
   laser at 1296.7: baseline decays to ~0 over minutes ⇒ residual N₂O
   confirmed (fix: shutoff valve in the analyte line, longer purges).
2. Toggle 1296.7 ↔ 1285.1 (true gap) with N₂O flowing: the 1285.1 level
   is the genuine structural background (+ any H₂O).
3. Repeat the narrow scan twice back-to-back: peak position shifting
   between runs ⇒ tuner/frequency instability quantified.

## ⚠ RETRACTED (27 Jul) — the "H₂O ruled out" verdict below was wrong

The ruling assumed room-temperature saturation (~3.5% at 600 Torr /
23 °C) versus a computed ~4.7% requirement and called the factor-1.35
gap "impossible by an order of magnitude." Two effects close the gap:
the chamber runs warm (saturation 5.3% at 30 °C) and the relevant H₂O
line at **1296.7093 cm⁻¹** is a hot line (E″ = 1475 cm⁻¹) whose strength
rises steeply with temperature. A water-saturated warm chamber yields
40–50 mV on this line. Moreover the 27-Jul three-point readings
(42 / 27 / 12 mV at nominal 1296.7 / 1297.1 / 1297.6) fit a *single*
line at ~1296.7 (monotonic decay, offset ≈ 0 today) and are
incompatible with the equal-strength N₂O comb at any offset. Leading
hypothesis: **liquid water condensed inside the gas system** (months of
sub-atmospheric humid-air ingress), re-saturating every sealed fill —
explaining purge immunity, evacuate–refill recovery, the minutes-scale
rise after fills, and the low (~6 mV) level under flow-through (flow
outruns the evaporation). Discriminating scan: H₂O doublet at
1296.49 + 1296.71 with silent R13/R14/R15 positions, versus the N₂O
0.78 cm⁻¹ comb. Credit: the water suspicion was the operator's,
raised a week earlier and wrongly dismissed by this analysis.

## Reference figure and the complete H₂O picture (27 Jul)

`h2o_n2o_1295-1300_hitran.par` (H₂O + N₂O, 1295–1300) →
`analysis/hitran_reference_plot.py` → `figures/hitran-n2o-h2o-reference.(png|pdf)`:
stick spectrum + simulated α at lab conditions (600 Torr, 25 °C, 100 ppm
N₂O vs saturated 4.0% H₂O).

Significant H₂O lines: **1296.490** (S = 1.72e-22 + 5.7e-23, E″ = 2010),
**1296.709** (3.63e-22, E″ = 1475), **1297.181/1297.184** (combined
3.0e-23, E″ = 2358). At saturation these give α comparable to 100 ppm
N₂O near 1296.5–1296.7 and a secondary feature at 1297.18 — **all three
27-Jul probe points (nominal 1296.7 / 1297.1 / 1297.6 → 42 / 27 / 12 mV)
land on water structure**, consistent with the condensed-reservoir
hypothesis with today's offset ≈ 0. Near **R15 the saturated-water α is
~350× below the N₂O peak** (and similar at R16): the proposed
operating-line move is quantitatively justified by this figure.

## H₂O ruled out for the 20-July evening background (superseded — see retraction above)

`h2o_n2o_1295-1298_hitran.csv` (fetched 20 Jul, H₂O + N₂O, 1295–1298):
the strongest H₂O line in the window is **3.6 × 10⁻²² at 1296.709**
(a hot line, E″ = 1475 cm⁻¹) — ~4,700× weaker than the N₂O R-branch
lines. Producing a 45 mV signal via H₂O here would require ~47% water
vapour; the saturation limit at 600 Torr / 23 °C is ~3.5%. **Physically
impossible → the steady 45–50 mV background at nominal 1297.6 cm⁻¹ is
not H₂O** (within 1295–1298; December's 1287.5/1288.5 peaks remain
genuine H₂O, outside this window).

Within 1295–1298 the only transitions strong enough to give tens of mV
at sub-% concentrations are the N₂O main-isotopologue R13/R14/R15 lines
(hot bands are 30× weaker). The economical hypothesis consistent with
all of tonight's facts: **N₂O still present in the ADM despite the
closed cylinder and 30-min "purge" (purge flow not exchanging the module
volume — plumbing/dead-volume question), combined with a shifted
instrument wavenumber offset after the evening retunes** (so nominal
1297.6 now sits on R15 at 1297.831 while nominal 1296.7 sits in the
R13–R14 gap). Offset shifts of ±0.1–0.2 between tuning sessions are
within EC-QCL set-point reproducibility.

**Decisive test (next session, ~18 min): narrow scan in pure N₂,
1295.3 → 1298.8, 0.1 steps, ~30 s/point.** If trapped N₂O: three
equal-height peaks at the R13/R14/R15 positions, and the peak positions
measure the current offset directly (free recalibration). A single peak
with silent neighbours would exclude N₂O (equal-S picket) and reopen the
search.

**RESOLVED (operator confirmation, 20 Jul evening): the ADM output valve
was never opened.** The module has been a dead-end volume all along —
supply-side gas switches changed the line composition but the ADM
interior only exchanged by slow diffusion, so the day's N₂O charge stayed
trapped through every "purge". This single fact explains: the steady
45–50 mV "N₂ background" (trapped N₂O read on R15), its immunity to the
closed cylinder and 30-min purge, the weak/confusing response to gas
switching in calibration legs 1–3, and (in part) historical anomalies —
the near-identical 6-July N₂ vs N₂O power sweeps and the December
"closed chamber" operating mode described in the methodology. Fix:
open the output valve → true flow-through. Confirmation scan above still
worth doing *before* opening the valve (trapped gas = free offset
calibration sample), then watch the decay at the R15 set point after
opening (purge time constant, second confirmation).

**Correction (21 Jul, morning):** the set-point bookkeeping of the late
evening was in error — the steady 45–50 mV trapped-gas reading and the
subsequent purge-decay monitoring were at nominal **1296.7** (= R14 with
the original −0.35 offset), not 1297.6. The "offset shifted" hypothesis
above is therefore unnecessary: everything is consistent with the
July-3 calibration unchanged (nominal 1296.7 = R14 at 1297.0501;
trapped charge ≈ 100 ppm reading ~45–50 mV exactly as 100 ppm did on
July 3; post-purge floor ~3 mV ≈ few-ppm residual + the known few-mV
optical background). Valve opened 21 Jul: flow-through purge dropped
the on-line background 45–50 → ~3 mV. Gap points for flat-background
checks with the −0.35 offset: nominal ≈ 1296.3 or ≈ 1297.1.
