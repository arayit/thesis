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

## Next

1. Needle ramp 200 → 600 Torr under flow at R15: separates
   pressure vs flow, measures the signal–pressure scaling, and picks
   the operating pressure with data.
2. Long stationary record at R15 (stability, Allan deviation).
3. Calibration series (concentration steps) → k [mV/ppm], linearity,
   LOD; then NNEA.
4. Methodology note: sealed-fill delivery failure + flow-mode
   requirement; per-session δ check (water peak, 10 min).
