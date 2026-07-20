#!/usr/bin/env python3
"""Concentration calibration: linear fit of net QEPAS signal vs N2O concentration.

Input: CSV with columns [conc_ppm, R_mV] (or [conc_ppm, R_min, R_max] — the
midpoint is used and the half-band becomes the error bar). The 0-ppm row, if
present, is treated as the background and subtracted from all points.

Usage: python calibration_fit.py calib.csv [--sigma-mv 0.5]
  --sigma-mv: 1σ baseline noise from a fixed recording (daq_timeseries.py);
              enables LOD = 3σ/k and 1σ-LOD output.
"""
import argparse

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--sigma-mv", type=float, help="1-sigma baseline noise in mV")
    args = ap.parse_args()

    rows = np.array([[float(v) for v in ln.replace(";", ",").split(",")[:3]]
                     for ln in open(args.csv)
                     if ln.strip() and ln.lstrip()[0].isdigit()])
    conc = rows[:, 0]
    sig = rows[:, 1] if rows.shape[1] == 2 else rows[:, 1:3].mean(axis=1)
    err = None if rows.shape[1] == 2 else (rows[:, 2] - rows[:, 1]) / 2

    bg = sig[conc == 0].mean() if (conc == 0).any() else 0.0
    net = sig - bg

    k, b = np.polyfit(conc, net, 1)
    resid = net - (k * conc + b)
    r2 = 1 - resid.var() / net.var()
    print(f"background (0 ppm): {bg:.2f} mV")
    print(f"slope k = {k:.4f} mV/ppm   intercept = {b:.3f} mV   R^2 = {r2:.4f}")

    if args.sigma_mv:
        print(f"LOD (1σ) = {args.sigma_mv / k:.3f} ppm")
        print(f"LOD (3σ) = {3 * args.sigma_mv / k:.3f} ppm")

    x = np.linspace(0, conc.max() * 1.05, 50)
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.errorbar(conc, net, yerr=err, fmt="o", ms=5, capsize=3, label="measured")
    ax.plot(x, k * x + b, "-", label=f"fit: {k:.3f} mV/ppm, $R^2$={r2:.4f}")
    ax.set_xlabel(r"N$_2$O concentration (ppm)")
    ax.set_ylabel("net QEPAS signal (mV)")
    ax.legend()
    fig.tight_layout()
    out = args.csv.rsplit(".", 1)[0] + "_fit.png"
    fig.savefig(out, dpi=150)
    print(f"plot: {out}")


if __name__ == "__main__":
    main()
