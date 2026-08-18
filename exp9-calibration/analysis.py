#!/usr/bin/env python3
"""Exp9 (3 Aug 2026, 17:20-18:08): concentration calibration at R15.

Protocol: two-MFC dilution at constant total flow 10 sccm, 205 Torr
constant flow. Ladder 100/80/60/40/25/10/5/0 ppm + return-to-100.
Per step: 60 s at the R15 peak (nominal 1298.1) and 60 s at the valley
reference (1297.7); signal = peak - valley (baseline-immune).
Nominal C from the metadata (set flows); actual MFC readbacks were not
logged.

Findings (see stdout + figure):
- k = 0.20-0.21 mV/ppm at 205 Torr (from the 100/80 pair + blank);
  sensor-noise LOD (1 sigma, 60 s) = 0.6 ppm.
- The mid/low ladder (5-60 ppm) reads systematically LOW vs nominal,
  progressively worse toward small mix-MFC flows. Sign analysis rules
  out settling (a descending ladder with slow exchange would bias
  HIGH); the pattern tracks the mix MFC toward its turndown floor
  (0.5-2.5 sccm) -> nominal concentration axis, not sensor response,
  is the prime suspect at low C. Next session: log MFC readbacks.
- Blank delta = +0.39 mV ~ optical-floor tilt between 1297.7 and
  1298.1 (~+0.2 mV in the exp7 blank) + <=1 ppm leak-through.
- Return-to-100: +5.1% vs initial (drift/hysteresis bound).

Output: figures/exp9-calibration.(png|pdf)
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CAL = HERE / "data"

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#1a1a19", "#6b6a63"


def read_point(path):
    wl = conc = start = None
    t, r = [], []
    for line in open(path):
        if line.startswith("#"):
            if "Laser.wavelength" in line:
                wl = float(line.split(",")[1])
            elif "Gas.concentration" in line:
                v = line.split(",")[1].strip()
                conc = float(v) if v else 0.0
            elif "start," in line:
                start = line.split(",")[1].strip()
            continue
        if line.startswith("iso_time"):
            continue
        p = line.strip().split(",")
        if len(p) >= 10:
            t.append(float(p[2]))
            r.append(float(p[9]) * 1000.0)
    t, r = np.array(t), np.array(r)
    core = r[t > 10.0]
    return start, wl, conc, np.median(core), core.std()


pts = sorted(read_point(f) for f in CAL.glob("qepas_*.csv"))
steps = []
for i in range(0, len(pts), 2):
    _, w1, c1, m1, s1 = pts[i]
    _, w2, c2, m2, s2 = pts[i + 1]
    assert abs(w1 - 1298.1) < 0.01 and abs(w2 - 1297.7) < 0.01 and c1 == c2
    steps.append((c1, m1 - m2, float(np.hypot(s1, s2))))

C = np.array([s[0] for s in steps[:8]])
D = np.array([s[1] for s in steps[:8]])
E = np.array([s[2] for s in steps[:8]])
cr, dr, er = steps[8]

# full-ladder linear fit (nominal axis)
A = np.column_stack([C, np.ones_like(C)])
(k_all, b_all), *_ = np.linalg.lstsq(A, D, rcond=None)
resid = D - (k_all * C + b_all)
r2 = 1 - (resid ** 2).sum() / ((D - D.mean()) ** 2).sum()

# trusted-anchor slope: 100/80 pair + blank
k_hi = (D[0] - D[7]) / 100.0
k_ret = (dr - D[7]) / 100.0
lod = 0.12 / k_hi
print(f"full-ladder fit : k={k_all:.4f} mV/ppm, b={b_all:+.2f}, R2={r2:.4f}, "
      f"resid rms {resid.std(ddof=2):.2f} mV (structured — see header note)")
print(f"anchor slope    : k={k_hi:.4f} (initial) / {k_ret:.4f} (return) mV/ppm")
print(f"sensor-noise LOD: {lod:.2f} ppm (1 sigma, 60 s);  3 sigma {3 * lod:.1f} ppm")
print(f"blank delta     : {D[7]:+.2f} +- {E[7]:.2f} mV;  return-100 "
      f"{100 * (dr - D[0]) / D[0]:+.1f}% vs initial")

fig, (ax, ax2) = plt.subplots(
    2, 1, figsize=(8.2, 6.4), sharex=True,
    gridspec_kw={"height_ratios": [2.6, 1.0], "hspace": 0.08})
fig.patch.set_facecolor("white")

cf = np.array([0, 105])
ax.plot(cf, k_hi * cf + D[7], color=BLUE, lw=1.6,
        label=f"anchor slope k = {k_hi:.3f} mV/ppm (100/80 + blank)")
ax.plot(cf, k_all * cf + b_all, color=MUTED, lw=1.0, ls="--",
        label=f"full-ladder fit (R$^2$ = {r2:.3f})")
ax.errorbar(C, D, yerr=E, fmt="o", ms=6, color=INK, mfc=ORANGE, mew=0.9,
            elinewidth=1.0, capsize=2.5, label="ladder (nominal C)", zorder=4)
ax.plot([cr], [dr], "D", ms=7, color=INK, mfc="white", mew=1.4,
        label=f"return to 100 ppm ({100 * (dr - D[0]) / D[0]:+.1f}%)", zorder=5)
ax.annotate("mix MFC 0.5–2.5 sccm:\nnominal axis suspect\n(turndown floor)",
            (25, 6.5), (42, 3.4), fontsize=8, color=MUTED,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.set_ylabel(r"$\Delta R$ = peak $-$ valley (mV)")
ax.set_ylim(-1, 24)
ax.legend(loc="upper left", frameon=False, fontsize=8.5)
ax.set_title("N$_2$O calibration at R15 — 205 Torr constant flow, "
             "total 10 sccm, 3 Aug 2026", fontsize=10.5, color=INK)

ax2.axhline(0, color=MUTED, lw=0.8)
ax2.errorbar(C, D - (k_hi * C + D[7]), yerr=E, fmt="o", ms=5, color=INK,
             mfc="white", mew=1.0, elinewidth=0.9, capsize=2)
ax2.set_ylabel("resid. vs anchor (mV)")
ax2.set_xlabel("nominal N$_2$O concentration (ppm)")
ax2.set_ylim(-4.5, 2)

for a in (ax, ax2):
    a.set_xlim(-3, 108)
    a.grid(True, alpha=0.18, lw=0.5)
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
    a.tick_params(labelsize=8.5, color=MUTED)

fig.tight_layout()
out = HERE / "exp9-calibration"
fig.savefig(f"{out}.png", dpi=200)
fig.savefig(f"{out}.pdf")
print(f"wrote {out}.png/.pdf")
