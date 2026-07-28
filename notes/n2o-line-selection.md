# R-branch notation, line selection, and the humidity consistency check

Working note, 28 Jul 2026. Feeds the thesis background chapter (line
selection rationale) and closes the water-background story. Sources at
the end.

## 1. What "R15" means

A mid-IR absorption line of a linear molecule like N₂O is a *combined*
vibration + rotation transition. The molecule goes up one vibrational
quantum (here the ν₁ symmetric stretch, band origin ~1285 cm⁻¹) and
simultaneously changes its rotational quantum number J by ±1 (ΔJ = 0 is
forbidden for a Σ–Σ band of a linear molecule):

- **R branch**: ΔJ = +1, written **R(J″)** where J″ is the *lower*-state
  J. Lines sit *above* the band origin. R15 ≡ R(15): J = 15 → 16.
- **P branch**: ΔJ = −1, written P(J″). Lines sit *below* the origin.
- Between P(1) and R(0) lies the **zero gap** at the band origin
  (~1285 cm⁻¹ for N₂O ν₁) — the only true "no-line" window nearby,
  which is why our off-line reference must go there or use gas exchange.
- The HITRAN label "R14e": the e is an e/f parity label; for a Σ⁺–Σ⁺
  band all levels are e — it carries no extra meaning here.

**Line spacing:** successive R-branch lines are ~2B apart (B = rotational
constant; for N₂O B ≈ 0.419 cm⁻¹ → ~0.84 cm⁻¹), shrinking slowly with J
(B′ < B″) — hence the observed ~0.78 cm⁻¹ picket spacing.

**Why R14–R16 are the strongest lines in the band:** line intensity
follows the Boltzmann population of the lower rotational level,
∝ (2J+1)·exp[−hcBJ(J+1)/kT], which peaks at

  J_max = √(kT/2hcB) − ½ ≈ √(205.7 / 0.838) − ½ ≈ **15**

for N₂O at 296 K. R15 is literally the most-populated rotational state's
transition. A practical corollary: **near the maximum, dS/dJ ≈ 0, so the
line strength is also first-order insensitive to room-temperature
drift** — lines far from J_max gain/lose strength as T changes, R15
barely moves.

## 2. Line-selection table (HITRAN 2020, actual wavenumbers)

| Line | ν (cm⁻¹) | S (cm/molec) | Nearest significant H₂O | Distance | Verdict (28-Jul scan) |
|---|---|---|---|---|---|
| R13 | 1296.2651 | 1.693e-19 | 1296.490 doublet (2.3e-22) | 0.23 | on water shoulder — avoid |
| R14 | 1297.0501 | 1.715e-19 | 1296.709 (3.6e-22) | 0.34 | ~20 mV water flank measured — avoid while wet |
| **R15** | **1297.8314** | **1.721e-19** | 1297.184 pair (3.0e-23) | 0.65 | **~1 mV over floor measured — clean** |
| R16 | 1298.6093 | 1.714e-19 | 1298.915 (1.5e-25) | 0.31 | clean (negligible neighbor) |
| R17 | 1299.3835 | 1.686e-19 | 1299.298 (7.9e-27) | 0.09 | clean (negligible neighbor) |

R15, R16, R17 are all experimentally clean in the 28-Jul saturated-water
scan. **R15 is the choice**: strongest S in the band, at the Boltzmann
optimum (T-robust), largest margin from the strong water complex, and
continuity with the December 2025 detection (which was R15). At today's
instrument offset (δ = −0.23) R15 sits at **nominal 1298.06**; re-measure
δ each session (a mini-scan over 1296.3–1297.3 across the water peak, or
over the N₂O comb once dry, calibrates it in ~10 min).

## 3. Humidity & room temperature: is the fitted water level consistent?

Fitted from the 28-Jul scan: p(H₂O) ≈ 24.7 Torr (4.1% of 600 Torr),
uncertainty dominated by the responsivity anchor → 19–31 Torr.

Equilibrium vapor pressure of liquid water: 18.7 Torr @ 21 °C,
23.8 @ 25 °C, 25.2 @ 26 °C, 31.8 @ 30 °C. So the fitted vapor equals
**equilibrium over liquid water at 25–26 °C (range 21–30 °C)** — exactly
the reported lab temperature ("not always cooled, warms to ~25 °C").
The chamber behaves as a sealed jar with a wet floor at room
temperature. Three independent checks:

1. **It cannot be the supply gas**: N₂ 6.0 carries ≤0.2 ppm H₂O
   (≤0.00012 Torr at 600 Torr) — 5 orders of magnitude below observed.
2. **It cannot be trapped lab air**: even *undiluted* lab air at 25 °C
   and 60% RH carries only ~14 Torr of water; at 100% RH, 23.8 Torr.
   The chamber shows ~25 Torr in a fill made from dry N₂ after
   evacuation. More water vapor than the room air itself can hold ⇒
   the source must be internal liquid in equilibrium.
3. **Reservoir budget**: at ~25 Torr in a ~0.1 L internal volume, each
   sealed fill consumes only ~2.4 mg of water. A single 50 µL droplet
   sustains ~20 fills; a visible ml-scale condensate lasts hundreds —
   explaining why weeks of purging never exhausted it. Kinetics agree
   too: minutes-scale rise after each fresh fill (evaporation into dry
   N₂), suppressed level (~6 mV) under flow-through (supply outruns
   evaporation).

**Verdict: yes — quantitatively consistent.** The July condensation
history is also plausible: pipes were left open to humid summer lab air
and the system runs sub-atmospheric (ingress direction), so moist air
entered and condensed in cold spots/low points over months.

## Sources

Accessible online explainers of P/R-branch structure:
- Chemistry LibreTexts, *Rovibrational Spectroscopy* —
  https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Spectroscopy/Rotational_Spectroscopy/Rovibrational_Spectroscopy
- Chemistry LibreTexts, *Rovibrational, vibronic, and rovibronic
  transitions* (§5.5, CHEM 110B) —
  https://chem.libretexts.org/Workbench/CHEM_110B:_Physical_Chemistry_-_Properties_of_Atoms_and_Molecules/05:_Spectroscopy_of_a_Molecule_in_Free_Space/5.05:_Rovibrational_vibronic_and_rovibronic_transitions

Citable references for the thesis (verify edition/pages when inserting):
- P. F. Bernath, *Spectra of Atoms and Molecules*, 3rd ed., Oxford
  University Press (2016) — linear-molecule rovibrational structure,
  Hönl–London factors, branch intensity distribution.
- G. Herzberg, *Molecular Spectra and Molecular Structure II: Infrared
  and Raman Spectra of Polyatomic Molecules*, Van Nostrand (1945) —
  the classic treatment; N₂O band structure.
- C. N. Banwell & E. M. McCash, *Fundamentals of Molecular
  Spectroscopy*, 4th ed., McGraw-Hill (1994) — gentlest introduction.
- I. E. Gordon *et al.*, "The HITRAN2020 molecular spectroscopic
  database," *J. Quant. Spectrosc. Radiat. Transfer* **277**, 107949
  (2022) — the line data used throughout this work.
- P. Patimisco, G. Scamarcio, F. K. Tittel, V. Spagnolo,
  "Quartz-Enhanced Photoacoustic Spectroscopy: A Review," *Sensors*
  **14**(4), 6165–6206 (2014) — QEPAS context.
