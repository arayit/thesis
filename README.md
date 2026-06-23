# M.Sc. Thesis — Özyeğin University (Electrical & Electronics Engineering)

LaTeX source for my Master of Science thesis. Written in English with IEEE-style
references. Designed to compile on **Overleaf** and to be version-controlled
with **Git/GitHub**.

> ⚠️ **Verify formatting against the official guide.** Margins, line spacing,
> page order, and the wording of the title/approval/declaration pages should
> match your Graduate School's official thesis-writing guide. Adjustable spots
> are flagged with comments in `preamble/style.tex` and `frontmatter/*.tex`.
> Official manuals & forms (cross-check your institute):
> <https://www.ozyegin.edu.tr/en/graduate-school-social-sciences/thesis-manual-forms>

## Project structure

```
thesis/
├── main.tex              # root document — Overleaf compiles THIS file
├── metadata.tex          # ✏️ your name, title, advisor, dates, keywords
├── references.bib        # bibliography (IEEE)
├── preamble/
│   ├── packages.tex      # \usepackage list
│   ├── style.tex         # margins, spacing, headers, heading styles
│   └── commands.tex      # custom macros
├── frontmatter/          # title, approval, declaration, abstract, acks
├── chapters/             # 01-introduction … 05-conclusion
├── appendices/           # appendix-a, …
├── figures/              # put images here (PDF/PNG/JPG)
├── .gitignore
└── latexmkrc             # local build config
```

## Editing checklist

1. Fill in **`metadata.tex`** (name, title, advisor, jury, dates).
2. Confirm margins / line spacing in **`preamble/style.tex`** match the guide.
3. Write your content in **`chapters/`**; add figures to **`figures/`**.
4. Add references to **`references.bib`** and cite with `\cite{key}`.

## Compiling

### On Overleaf (recommended)
Menu ▸ **Main document** = `main.tex`, **Compiler** = `pdfLaTeX`.
Overleaf runs `biber` automatically — just press **Recompile**.

### Locally (optional)
Needs a TeX distribution (e.g. MacTeX) with `pdflatex` + `biber`:
```bash
latexmk -pdf main.tex     # full build (LaTeX → biber → LaTeX ×2)
latexmk -c                # clean aux files
```

## GitHub ↔ Overleaf

Three ways to connect this repo to Overleaf — pick one:

**A. Import from GitHub (simplest).** On Overleaf: **New Project ▸ Import from
GitHub**, choose this repository. (Requires linking your GitHub account;
GitHub sync is a paid Overleaf feature.)

**B. Overleaf's built-in Git (works on free plans).** Create a blank Overleaf
project, then **Menu ▸ Git** to get its git URL, and push this repo's contents
to it.

**C. Upload a ZIP.** **New Project ▸ Upload Project** with a zip of this folder.
Quick, but no two-way sync afterwards.

Once linked, you `git push`/`git pull` (or use Overleaf's Sync button) to move
changes between your machine, GitHub, and Overleaf.

## Pushing to GitHub the first time

```bash
# create an empty repo on github.com first (no README/.gitignore), then:
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```
