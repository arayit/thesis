# Exp 6 — N₂O DETECTED: R15 line under constant flow (3 Aug 2026, 13:56–14:11)

**Files:** `exp6-scan/` — fine scan nominal 1297.5–1298.5, 0.1 steps,
30 s/point (TC 3 s, sens 200 mV), **100 ppm N₂O mix in constant flow**,
needle valve at the ADM output, **205 Torr**, ~3.3 mW; plus a water
check point at nominal 1296.9. Operator control (not in files):
switching the supply N₂O → N₂ at nominal 1298 decayed the signal
26 → 9 mV.

**Analysis:** `analysis/exp6_r15_line.py` → `figures/exp6-r15-line.(png|pdf)`.

## Result — first N₂O detection since December 2025

A clean absorption line: 6.5–7.5 mV floor rising to 29.1 mV at nominal
1298.1. All identification criteria met simultaneously:

| Criterion | Expected | Measured |
|---|---|---|
| Position | R15 (1297.8314) at nominal 1298.05–1298.07 (δ ≈ −0.23) | peak at 1298.05, **δ = −0.22** |
| Width | laser-limited 0.24–0.28 cm⁻¹ (molecular width 0.04 at 205 Torr) | **0.24 cm⁻¹** |
| Amplitude | ~16–25 mV over floor for 100 ppm at 205 Torr (anchor ±30–40%, Q(205)>Q(600)) | **+22 mV**; anchor-based ≈ 125 ppm ≈ nominal within systematics |
| Causality | signal must follow the gas | **N₂O → N₂ switch: 26 → 9 mV** |
| Water sanity | flow-suppressed water at 1296.9 (~6–15 mV historical flow value) | 14.8 mV ✓ |

Fit R² = 0.989. δ = −0.22 vs −0.23/−0.24 on 28/31 Jul — the set-point
offset is stable across sessions this week.

## What made the difference

Same cylinder, same laser, same QTF, same wavelengths as the null
results of 31 Jul. Two things changed together: **constant flow**
(needle valve at ADM output, supply flowing continuously) and
**205 Torr** instead of 600. The 31-Jul sealed-fill points (overlaid in
the figure) are flat through the identical window. Every historical
success (Dec 2025, 3 Jul, the 20-Jul trapped charge) also had long
gas–cell contact or continuous flow; every null was a fresh sealed fill
measured within minutes. Pending the needle-valve pressure ramp
(200 → 600 Torr under flow, signal ∝ P expected for our broad-laser
regime), the enabling variable is most consistent with **gas delivery
under flow** rather than pressure itself. The sealed-fill delivery
failure remains an open mechanism question — operationally moot in
flow mode, but worth a paragraph in the thesis methodology.

## Exp 7 / Exp 8 — blank vs analyte full-window pair (15:20–16:51)

**exp7-scan/**: pure N₂ blank, nominal 1295.0–1300.0, 0.1 steps,
30 s/point, ~200 Torr constant flow (10 sccm). Closing anchor at
1295.0: +0.04 mV over 42 min. **Operator note: lab at 21 °C, 75% RH.**
**exp8-scan/**: identical grid with the 100 ppm N₂O mix. Closing anchor
−0.85 mV. *Metadata correction:* `Gas.gas_type` in several early exp8
files reads "N2" (logger field not updated at session start); the
flowing gas was the N₂O mix throughout — identity assigned per
experiment, not per header. First ~2 points carry a small
post-switch equilibration transient.

**Analysis:** `analysis/exp78_comb_fit.py` → `figures/exp78-comb.(png|pdf)`.

### Result — the complete R-branch comb

The point-by-point difference exp8 − exp7 (water background and optical
floor cancel) shows **six pickets, R12–R17, at 0.78 cm⁻¹ spacing**, all
at the HITRAN positions with δ = −0.23 (fourth consecutive session at
−0.22…−0.24). Diff-fit R² = 0.888 — limited by steep-flank sampling
(±0.01 cm⁻¹ set-point reproducibility ≈ ±2 mV on 200 mV/cm⁻¹ flanks),
not by noise. Picket amplitude ≈ 78 ppm-equivalent on the 600-Torr
responsivity anchor (exp6 fine scan gave ≈ 125): both within the
anchor's ±30–40% systematic (Q rises at 205 Torr; lineshape-width
coupling) — i.e. **consistent with the nominal 100 ppm**; the real
concentration axis comes from the upcoming calibration ladder.

The blank (exp7) documents the flow-mode background: 5–7 mV optical
floor + flow-suppressed water (~+7 mV at nominal 1296.9, vs ~50 mV in
sealed mode — the supply outruns reservoir evaporation, as inferred
on 21 Jul).

### Humidity closure (measured room data at last)

Lab: 21 °C, 75% RH → lab-air water partial pressure 0.75 × 18.7 =
**14.0 Torr** (dew point ≈ 16.3 °C). The sealed-chamber fits of
28/31 Jul gave ~25 Torr — **1.8× more water than the lab air itself
carries**, now with measured (not assumed) room conditions: the
internal liquid-reservoir mechanism is confirmed quantitatively.
`notes/n2o-line-selection.md` §3 updated.

## Exp 9 — concentration calibration at R15 (17:20–18:08)

**exp9-calibration/**: two-MFC dilution at constant total 10 sccm,
205 Torr flow. Ladder 100/80/60/40/25/10/5/0 ppm + return-to-100;
per step 60 s at the peak (nominal 1298.1) and 60 s at the valley
(1297.7); signal = peak − valley. Nominal C in the metadata; MFC
readbacks not logged (next time!).

**Analysis:** `analysis/exp9_calibration.py` → `figures/exp9-calibration.(png|pdf)`.

### Results

- **k ≈ 0.20 mV/ppm at 205 Torr** (anchor slope from the 100/80 pair +
  blank: 0.201 initial / 0.212 on return). Full-ladder linear fit
  R² = 0.980 with *structured* residuals (below).
- **Sensor-noise LOD = 0.6 ppm (1σ, 60 s point)**; 3σ ≈ 1.8 ppm.
- **Blank Δ = +0.39 ± 0.12 mV** ≈ optical-floor tilt between the two
  wavelengths (+0.2 mV in the exp7 blank) + ≤1 ppm mix leak-through.
- **Return-to-100: +5.1%** vs initial (session drift/hysteresis bound).
- **Preliminary NNEA ≈ 3×10⁻⁸ W·cm⁻¹·Hz⁻¹ᐟ²** (α_min(1σ) ≈ 2×10⁻⁶ cm⁻¹
  at 3.3 mW, ENBW ≈ 0.04 Hz for TC 3 s) — same decade as the
  Patimisco-family QEPAS literature. Refine after the Allan record.

### The mid-ladder systematic (honest accounting)

Steps 5–60 ppm read progressively LOW vs nominal (worst −2.8 mV at
25 ppm), while 80/100 are mutually proportional to 0.5%. Settling
cannot explain it: on a *descending* ladder, incomplete exchange biases
readings HIGH. The deviation instead tracks the mix MFC toward its
turndown floor (2.5 → 0.5 sccm setpoints), so the prime suspect is the
**nominal concentration axis (mix-MFC underdelivery at small flows)**,
not sensor nonlinearity — QEPAS response is linear in this range
throughout the literature (e.g. Menduni 2023, 1–10 ppm). Action:
repeat the 5–40 ppm steps logging MFC *readbacks* (or verify the mix
MFC at 0.5–2.5 sccm independently) before the thesis-final calibration
figure.

## Next

1. Re-run 5–40 ppm ladder steps with MFC readbacks logged.
2. Blank Allan deviation at R15 (20–30 min on N₂) → formal LOD + NNEA.
3. Needle ramp 200 → 600 Torr under flow at R15: pressure-vs-flow
   separation + signal–pressure scaling.
4. Methodology note: sealed-fill delivery failure + flow-mode
   requirement; per-session δ check (water peak, 10 min).
