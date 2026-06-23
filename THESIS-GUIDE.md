# Thesis Guide — scope, setup, and how it differs from a paper

A practical guide for *this* thesis. You've written a research article before but
not a thesis, so the most useful starting point is the difference between the two
(Section 2), then the concrete scope (Section 1) and structure (Section 4).

---

## 1. Your thesis in one sentence (the scope)

> **I designed, built, and experimentally characterized a pulsed-QCL QEPAS sensor,
> and validated it by detecting N₂O — quantifying its sensitivity, detection
> limit, and stability — as a platform toward future trace-VOC sensing.**

- **Contribution = the working instrument + its characterization.** For an
  experimental MSc, *building and validating a sensor is the contribution.* You
  do not need a novel algorithm or a new theory on top.
- **N₂O is the validation gas, not the goal.** It has strong, well-documented
  lines, so it lets you benchmark the system cleanly.
- **Plant VOC detection is future work / motivation**, not part of this thesis.
  Keep it out of scope — it's your next paper, and it makes a great closing chapter.

### In scope
System design & integration · alignment · ADM/QTF characterization (f₀, Q) ·
lock-in characterization · QCL characterization (power, tuning) · optical power
budget · N₂O line selection (HITRAN) · N₂O detection + concentration calibration ·
sensitivity (NNEA), minimum detectable concentration, Allan deviation.

### Out of scope (say so explicitly, then stop)
Plant VOC measurements · designing custom electronics if you used a commercial
ADM · exhaustive comparison of every possible laser/line. Naming what you
*didn't* do is a sign of a mature thesis, not a weak one.

> **Is it enough?** Yes — comfortably. The risk with this topic was never "too
> small"; it was "too vague." The scope above fixes that.

---

## 2. Thesis vs. research article — what actually changes

You know how to write a paper. A thesis is **not a long paper**; it has a
different purpose and reader. Keep these differences in mind:

| Aspect | Research article | MSc thesis |
|---|---|---|
| **Reader** | Expert peers | An examiner + future students; assume *less* prior knowledge |
| **Goal** | Report a novel result concisely | Demonstrate *you* mastered the topic and did the work properly |
| **Background** | A few paragraphs | A full chapter — teach the reader QEPAS from the ground up |
| **Methodology** | Compressed, "see refs" | Detailed enough to **reproduce** your setup; include alignment, budgets, settings |
| **Length** | ~6–12 pages | Tens of pages (quality over page count — don't pad) |
| **Negative/partial results** | Usually omitted | Welcome — what didn't work and why is valuable |
| **Voice** | Terse, impersonal | Still formal, but more explanatory and didactic |
| **Defense** | None | You defend it orally — write so you can present every figure |

**Practical upshot:** expand the *Background* and *Methodology* far beyond paper
length, justify every choice (why this line? why this f₀? why this τ?), and make
the setup reproducible. The Results chapter is closest to paper-style.

---

## 3. Setup of the work (how to run the project)

1. **Lock the scope** (Section 1) with your advisor *before* writing much. Get
   them to confirm the one-sentence statement and the in/out-of-scope lists.
2. **Build the skeleton first** — this repo already has it. Fill section stubs
   with bullet points, then prose.
3. **Write results as you measure.** Each characterization you finish (f₀/Q,
   lock-in, QCL, power budget) becomes a section *now*, while details are fresh.
4. **Keep a lab log** of settings and dates — it makes the Methodology chapter
   write itself and protects you in the defense.
5. **Cite as you go** into `references.bib`; never leave citations for the end.

---

## 4. Structure (maps to the chapters in this repo)

1. **Introduction** (`chapters/01`) — motivation (N₂O as greenhouse gas + path to
   VOC), problem statement, objectives, contributions, outline. *Drafted for you.*
2. **Background** (`chapters/02`) — photoacoustics → QEPAS → pulsed AM/1f detection
   → figures of merit (NNEA) → N₂O spectroscopy & line selection → related work.
3. **Sensor Design & Setup** (`chapters/03`) — block diagram, pulsed QCL & tuning,
   AM detection scheme, ADM, alignment, **optical power budget**.
4. **Results & Discussion** (`chapters/04`) — ADM/QTF char (f₀, Q), lock-in char,
   QCL char, power budget, N₂O scan + calibration, sensitivity (NNEA/MDL), Allan
   deviation, discussion vs. literature.
5. **Conclusion & Future Work** (`chapters/05`) — summary + headline numbers →
   plant-VOC direction & publication.

Front matter (title, approval, declaration, abstract, acknowledgements) is
already scaffolded; the abstract is written *last*.

---

## 5. Suggested writing order

Don't write front-to-back. Write in the order the material is solid:

1. **Methodology** (you know your setup best) →
2. **Results** (as data arrives) →
3. **Background** (fill the theory the reader needs to follow you) →
4. **Introduction** (now you know exactly what you did — refine the draft) →
5. **Conclusion** → 6. **Abstract** (last, ~150–300 words).

---

## 6. Practical conventions (already set up in this repo)

- **Compile:** Overleaf (Main document = `main.tex`, Compiler = pdfLaTeX), or
  `latexmk -pdf main.tex` locally.
- **Edit `metadata.tex`** for title/name/advisor/jury/dates.
- **Units:** use `siunitx` — `\SI{4.5}{\micro\meter}`, `\SI{1}{\mega\hertz}`.
- **Formulae:** `\nto`, `\cotwo`, `\water` macros are defined.
- **Figures:** vector PDF where possible; put files in `figures/`.
- **References:** IEEE via biblatex; cite with `\cite{key}`.
- **`\todo{...}`** marks open spots in red — search for them before submitting.
- **⚠️ Formatting:** margins/spacing/title-page wording follow common Turkish
  conventions, *not* a verified official template. Cross-check against your
  Graduate School's thesis guide and adjust `preamble/style.tex` / `frontmatter/`.

---

## 7. Before you submit — checklist

- [ ] All `\todo{}` markers resolved (incl. QCL wavelength / N₂O line)
- [ ] Every figure/table referenced in the text and discussed
- [ ] Margins, spacing, page order match the official guide
- [ ] All citations verified (volumes, pages, DOIs — some `.bib` entries are marked "VERIFY")
- [ ] Abstract written and within the word limit
- [ ] Title page, approval page, declaration filled in
- [ ] Spell-check + a full read-through aloud
- [ ] Advisor sign-off on the final draft
