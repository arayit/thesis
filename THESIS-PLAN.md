# Thesis Completion Plan

Working roadmap for finishing the pulsed-QCL QEPAS / N₂O thesis. Living document,
update as things get done. Last updated: 2026-06-24.

Companion to `THESIS-GUIDE.md` (scope and how-to). This file tracks *what is left*.

---

## 1. Status snapshot

| Chapter | State | What is left |
|---|---|---|
| 1 Introduction | ~90% | one citation flag (GWP/ozone); final read |
| 2 Background | ~85% | two citation flags (pulsed-QCL broadening, HITRAN); optional schematic figures |
| 3 Design & Setup | ~75% | real figures (block diagram, focusing); component/method citations |
| 4 Results & Discussion | ~40% | final measurements + the four figures of merit; real plots |
| 5 Conclusion | ~10% | write (after results are final) |
| Abstract | 0% | write last (~150–300 words) |

Body text is currently ~4,600 words (roughly 25–35 compiled pages). 0 real figures
so far (4 placeholder boxes).

---

## 2. Remaining lab work (the critical path)

- [ ] Re-align the beam through the ADM. The current detection limit is set by a
      large wavelength-independent background from imperfect alignment (§4.8), so
      better alignment should lower it and improve the NNEA. Record before/after.
- [ ] N₂O signal vs concentration → calibration curve, sensitivity (slope), R².
- [ ] N₂O signal vs laser power → confirms S ∝ P₀ (§2.1); needed to normalize NNEA.
- [ ] No-gas / non-absorbing-line background → noise floor → MDL and NNEA.
- [ ] **One long fixed-condition recording for the Allan deviation (≥ 1000 s).**
      Easy to forget. It is a separate measurement, not a sweep, and it is already
      promised in the objectives (Ch. 1) and §2.4. Grab it while the rig is set up,
      otherwise it is a second trip to the lab.

Estimated a few weeks of lab work if alignment goes well. Analysis and figures are
what usually drag afterward; staging them in parallel (Section 7) avoids that.

---

## 3. Measurements → thesis deliverables

- Concentration sweep → calibration curve + sensitivity + linearity (R²).
- Power sweep → S ∝ P₀ check + power normalization for NNEA.
- No-gas / background → noise floor → minimum detectable concentration + NNEA.
- Long fixed recording → Allan deviation → optimal integration time + best stability.

---

## 4. Integration time and figures of merit (reference)

"Integration time" means two different things here:

1. **Lock-in time constant τ** (a knob on the EG&G 5110). The integration time of a
   single reading. It sets the detection bandwidth Δf. Longer τ = less noise, slower.
2. **Allan averaging time** (an analysis variable, not a setting). Record one long
   stream, then compute the deviation vs averaging window. White noise falls as
   1/√τ until drift takes over and it rises. The minimum is the *optimal integration
   time* and the best detection limit.

**Time constant → bandwidth (needed for NNEA):**
- single-pole filter (6 dB/oct): Δf = 1/(4τ)
- two-pole filter (12 dB/oct): Δf = 1/(8τ)
- Check which slope the 5110 uses. Record τ and slope for every run.

**NNEA:**

    NNEA = α_min · P / √Δf      [cm⁻¹ · W · Hz^(−1/2)]

where α_min is the smallest detectable absorption coefficient (SNR = 1, from the
calibration plus the no-gas noise), P is the optical power at the fork, and Δf comes
from the time constant above. Converting concentration to α needs the HITRAN line
strength (the open §2.5 citation).

**Practical recipe:**
- Calibration sweeps: τ ≈ 100 ms – 1 s for a steady reading; note τ and slope.
- Allan: short τ, log the output every 0.1–1 s for ≥ 1000 s, let the math average.
- **Caution:** avoid the sensitivity ranges that read ~40% high at τ ≥ 30 ms (§4.2),
  or the noise floor is biased.

---

## 5. Figures to add

- [ ] 3D Blender render of the setup — *you*
- [ ] 2D system block diagram with the lock-in chain — *you* (Claude can do a TikZ version)
- [ ] Focusing guide + Gaussian-beam calculation figure — *Claude can draft from §3.5*
- [ ] QCL output power / tuning + calibration curve — *Claude from `experimental/*.xlsx`*
- [ ] Results plots, replacing the placeholder boxes:
  - [ ] ADM/QTF resonance (f₀)
  - [ ] Lock-in linearity
  - [ ] N₂O signal vs concentration (calibration)
  - [ ] Water-vapour / HITRAN interference
  - [ ] Allan deviation
  - [ ] (signal vs power, background vs alignment)

---

## 6. Open citation flags

- [ ] Intro — N₂O GWP value + dominant-ozone-depleter claim (e.g. IPCC AR6, Ravishankara 2009)
- [ ] §2.3 — intrapulse heating / spectral broadening in *pulsed* QCLs
- [ ] §2.5 — HITRAN (e.g. Gordon et al. 2022, JQSRT). Also clears the lone `[?]` in Results.

Find them all with: `grep -rn '\needcite' chapters`

Already cited (verified, in `references.bib`): Bell 1880, Kosterev 2002, Miklós 2001,
Dong 2010, Ma 2013, Patimisco 2014, Lin 2023, Sampaolo 2022, Wu 2017, Wang 2024,
Chen 2025.

---

## 7. Analysis / writing tasks Claude can do now

- [ ] Allan-deviation + NNEA + calibration script (logged data → numbers + plots)
- [ ] Focusing-guide subsection for §3.5 + beam-radius-vs-position figure
- [ ] Plot the QCL power/tuning curve from `QCL Characterization.xlsx`
- [ ] Draft the Conclusion against current content (placeholders for final numbers)
- [ ] Write the Abstract (last, once results are final)

---

## 8. Page target (guide, not a quota)

| Chapter | Target pages |
|---|---|
| 1 Introduction | 4–6 |
| 2 Background | 10–15 |
| 3 Design & Setup | 12–18 |
| 4 Results & Discussion | 15–22 |
| 5 Conclusion | 3–5 |
| **Body total** | **~45–65** |

With front matter, references, and appendices: roughly **60–85 pages total**. Quality
over count; an experimental thesis earns its pages through figures, tables, and real
measurements in Chapters 3–4. Confirm any official minimum/format with the Özyeğin
graduate-school guide.

---

## Key numbers (handy reference)

- QTF resonance / modulation: f₀ = 12458.8 Hz
- QCL: Daylight Solutions MIRcat-2300, 1111–2000 cm⁻¹ (5–9 µm)
- N₂O lines: 1297.8 cm⁻¹ (primary, ≈7.7 µm), 1271.5 cm⁻¹ (secondary), ν₁ band
- Focused waist ≈ 100 µm, Rayleigh range ≈ 4.1 mm; two-window transmission ≈ 87.2%
- Working point used: ~20 mW at 1000 ns; chamber 500–600 Torr; 50–100 ppm N₂O
