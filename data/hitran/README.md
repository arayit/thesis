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

(Caveat: this dataset contains no H₂O lines; H₂O interference near the
operating region is documented separately in Results §h2o and is not
excluded by these tests.)
