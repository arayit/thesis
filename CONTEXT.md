# CONTEXT.md — QEPAS N₂O Thesis Project

> Handoff context for Claude Code sessions. Read this + THESIS-PLAN.md first.
> Last updated: 2026-07-07 (from claude.ai sessions, June–July 2026).

## What this project is

MSc thesis (Özyeğin University, `ozu-thesis.cls`, compile with pdflatex):
a pulsed-QCL quartz-enhanced photoacoustic spectroscopy (QEPAS) sensor for
N₂O detection. Thesis LaTeX lives in this repo; experimental raw notes in
`experimental/`; roadmap in `THESIS-PLAN.md` (§2b has the agreed phased plan).

## Experimental system (as built)

- **Laser:** Daylight Solutions MIRcat (pulsed-only head), 1111–2000 cm⁻¹.
  Externally triggered by Rigol DG922 Pro CH1 (pulse mode, 50 Ω load setting)
  at the QTF resonance. Pulse width 100–1000 ns typical; duty-cycle limit 5%,
  max width 1 µs. Absolute wavelength accuracy ±0.5 cm⁻¹; pulsed linewidth
  <1 cm⁻¹ (this matters — see "line location" below).
- **Detection:** Thorlabs ADM01 acoustic detection module (QTF + integrated
  preamp, BaF₂ wedged windows) on a PY005 5-axis stage. Signal → EG&G 5110
  lock-in. Lock-in reference: DG922 CH2 dummy reference (fixed 500 ns width,
  phase offset ≈217.4° compensating QCL internal delay) because TRIG OUT
  fails to lock below ≈400 ns pulse width.
- **Gas line:** Alicat MFCs (10 sccm analyte: certified 100 ppm N₂O in N₂;
  200 sccm N₂ buffer) → Alicat PCD-15PSIA pressure controller → ADM →
  Vacuubrand pump. Typical chamber pressure 500–600 Torr.
- **Focusing:** plane mirror → OAP MPD149-M01 (RFL 101.6 mm) → ADM.
  Beam-propagation simulation: `beam_propagation.py` (LightPipes; lives
  outside repo currently — should be added under `analysis/`).

## Key measured results so far

| Quantity | Value | Where |
|---|---|---|
| QTF resonance f₀ | 12458.83 ± 0.01 Hz (ambient) | ADM char., Lorentzian fit |
| QTF Q factor | 9007 ± 91 (100 mV drive); 7963 ± 118 (50 mV) | linear-drive regime confirmed (peak ratio 0.52 vs 0.50) |
| Background power linearity | R² = 0.989 over 0.8–5.4 mW | proves photoacoustic origin |
| Electronic floor (laser off) | ≈0.1 mV | negligible pickup |
| ADM transmission (measured) | ≈85% (predicted windows-only: 87.2%) | residual structural loss 2–3% |
| **N₂O line located** | **peak at nominal 1296.7 cm⁻¹** (target was 1297.0; offset −0.3, within ±0.5 spec) | wavelength scan, 100 ppm, 600 Torr: peak 36 mV vs ~4 mV baseline, 4 consecutive elevated points 1296.6–1296.9 |
| Focus geometry | w_focus ≈ 89 µm, z_R ≈ 3.3 mm, beam ≈355 µm at tube far end vs 800 µm tube radius → centered clipping ~0.004% | beam_propagation.py + analytic check |
| Decenter tolerance | 2–3% loss ↔ ~400–450 µm lateral offset; target ±100–150 µm after alignment | analytic |

## OPEN QUESTIONS (carry into next lab day — Period A1)

1. **45-vs-12 mV background discrepancy:** identical conditions (500 ns,
   ~3.3 mW, 1297.0, 600 Torr) gave 45 mV in the 6-July power sweeps but
   12 mV in the same-day wavelength scan. Unresolved. Check first:
   (a) was the lock-in display reading R (magnitude) or X (in-phase)?
   Scan values hitting exactly 0 mV suggest X. (b) which sensitivity range
   was each dataset on? Documented artifact: sens 500 µV / 5 mV / 50 mV read
   ~40% high at TC ≥ 30 ms.
2. **Gas on/off (park & switch) not yet done** — the peak at 1296.7 is
   strong evidence but not yet proof of gas attribution. First lab task.
3. **QCL→OAP distance ~1.5 m (estimated, not measured)** — measure; input
   beam size at OAP assumed w₀ = 2.75 mm in simulation, 2.5 mm in thesis
   text. Harmonize after measuring.
4. **HITRAN line identification for the 1296.7 peak** — desk work, pending.
   Peak may be an unresolved multiplet (laser linewidth < 1 cm⁻¹ vs 0.8 cm⁻¹
   line spacing).

## Conventions / decisions already made

- Detection scheme: **1f amplitude modulation** (pulsed-only laser → 2f-WMS
  hardware-impossible; justified vs. Sampaolo et al., Photoacoustics 21
  (2021) 100219 — same scheme). Background handled by on-line/off-line
  subtraction, not 2f.
- Lock-in TC = 3 s within any one dataset (wait ≥15 s per point);
  Δf = 1/(4·TC) for NNEA. Record TC + sens + display quantity with every
  dataset. Sens fixed within a scan (100 mV typical); avoid artifact ranges.
- Note min–max of fluctuating readings, record the midpoint (never the peak).
- Daily reference measurement at session start: line centre, pure N₂,
  500 ns, TC 3 s, sens 100 mV.
- LOD to report: 3σ/k (also quote 1σ for literature comparison);
  NNEA = α·P_avg/(SNR·√Δf); P_avg = peak power × duty cycle.
- Thesis: nominal set-point wavenumbers are instrument values, not absolute;
  always state the located offset.

## Immediate repo tasks (first Claude Code session)

1. ~~Merge `methodology-updates.tex` into `chapters/03-methodology.tex`~~
   DONE 2026-07-06 (sec:line-location + sec:validation-protocol added; edit
   list applied except w₀, pending measurement). Overleaf compile check
   still needed (no LaTeX toolchain in the remote container).
2. ~~Fix stale numbers per that edit list~~ DONE 2026-07-06 in ch. 3 +
   sec:adm-char (Q written in). Historical 1297.8 values in ch. 4 and the
   "line used for detection is at 1297.8" sentence in ch. 2 §2.5 left as-is
   → rewrite in Period C with the located-line language.
3. `analysis/` created with README; fit scripts (QTF Lorentzian fit,
   power-linearity fit, wavelength-scan plot) + `beam_propagation.py`
   still to be moved in — they live outside this repo.
4. HITRAN line identification for 1296.7 (needs HITRAN data access) → feeds
   sec:line-location cross-ref + Results §h2o.
5. `grep -rn '\needcite' chapters frontmatter` → 19 flags on ~14 lines
   remain (list in THESIS-PLAN.md §5).

## Data files (in experimental/ and from claude.ai sessions)

- `Experiments__new__1_.xlsx` (claude.ai upload): sheets = 1 July power sweep;
  6 July-1 (N₂, 600 Torr) and 6 July-2 (100 ppm N₂O) power sweeps — nearly
  identical (laser was parked between lines, mystery solved by the scan);
  July-3 = the wavelength scan that found the 1296.7 peak.
- `ADM_Characterization*.xlsx`: QTF resonance sweeps (100 & 50 mV drive).
- Figures already generated (regenerate via scripts once in `analysis/`):
  QTF Lorentzian fits, drive comparison, power linearity, N₂O wavelength scan.
