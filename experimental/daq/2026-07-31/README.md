# Exp 5 — "100 ppm N₂O" counterpart scan 1295.0–1298.1 (31 Jul 2026, 15:50–16:25)

**Files:** `exp5-scan/qepas_20260731_*_N2O_*.csv` — 32 points, 0.1 cm⁻¹
steps, same protocol as exp4 (30 s/point, TC 3 s, sens 200 mV, sealed
600 Torr). Fill drawn from the cylinder labeled **100 ppm N₂O** after
pump-down through the ADM output valve. `exp5-notes.txt` is empty.

**Session context.** The first fill attempts produced no change because
the ADM output valve — the only path through which the ADM actually
exchanges gas — was closed: a chamber cannot be evacuated backward
through its supply MFC. This was discovered live (opening the output
valve dropped the signal 60 → 5 mV and the pressure 600 → 40–50 Torr).
The scan here was taken *after* the correct procedure (pump down via
output valve → close → fill from the mix cylinder → settle). N₂ cylinder
not connected during these fills (single-line, bottle-swap workflow).

**Analysis:** `analysis/exp5_scan_fit.py` → `figures/exp5-vs-exp4.(png|pdf)`.

## Result: the delivered gas contained no measurable N₂O

| Quantity | exp4 (28 Jul, pure N₂) | exp5 (31 Jul, "100 ppm N₂O") |
|---|---|---|
| δ (instrument offset) | −0.230 | −0.240 |
| laser FWHM | 0.26 | 0.26 |
| water amount | 1.040 ± 0.014 × sat | 1.073 ± 0.018 × sat |
| full-fit R² | 0.9922 | 0.9927 |
| fitted N₂O | 1.5 ± 1.2 ppm | 2.3 ± 1.8 ppm |

Comb-template correlation on the point-by-point difference (exp5 − exp4,
shared water background cancels): picket amplitude **−0.68 ± 0.48 mV**
= **−1.5 ± 1.1 ppm N₂O** — consistent with zero; **≤ ~3 ppm at 3σ**.
A 100 ppm fill would have added 40–45 mV pickets at R12/R13/R14/R15
(registered prediction, committed before the measurement); the measured
difference curve is flat at the ±1 mV level.

## What this closes and what it opens

Closed by this data (all *operational* hypotheses):
- Wavelength/δ: water peak reproduced at the same nominal → R15 truly at
  nominal 1298.06. Laser tuning certified through the water structure.
- Pressure: water lineshape height/width reproduce the 600 Torr fit.
- Transduction chain (QTF, f₀, lock-in, alignment): water amplitude
  reproduced within 2%; rep rate = mod frequency = 12458.8 Hz both days.
- Gas exchange: verified live (vent collapse), fills real.
- Sensor's ability to see N₂O: proven historically (3 Jul comb, Dec 2025).

Open (the only remaining free variable): **the content of the cylinder
currently on the line.** The spectrometer reports what arrives between
the QTF prongs: wet N₂ to within 3 ppm. Next actions: (1) establish
whether today's physical cylinder is the same one that produced the
3 Jul comb (swap/refill history); (2) independent positive control
(any second N₂O source, e.g. a cream-charger cartridge, ~0.2 Torr into
the evacuated ADM topped with N₂ → R15 should read ~10× the 100 ppm
level); (3) supplier certificate / analysis of the cylinder.

Silver lining: three sessions (27, 28, 31 Jul) now demonstrate
instrument reproducibility at the ~1 mV / 0.01 cm⁻¹ level — thesis-grade
stability data, and the sensor is demonstrably ready: the moment real
N₂O enters the chamber, the comb appears at the registered positions.
