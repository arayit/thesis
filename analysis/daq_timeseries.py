#!/usr/bin/env python3
"""Analysis for DAQ time-series recordings from the 5110 lock-in CH1/CH2 outputs.

Input: CSV with columns [time, ch1_V] or [time, ch1_V, ch2_V]; header optional.
Time may be seconds or ISO timestamps. Conversion: R_mV = ch1_V * SENS_MV
(CH1 full scale = 1 V = sensitivity; 5110 manual §3.3.23).

Usage:
  python daq_timeseries.py record.csv --sens 100 [--events events.txt]

events.txt lines: "HH:MM:SS  label"  (e.g. "14:32:00 switch to N2"),
used to split the record into segments and report per-segment stats.

Outputs: per-segment mean / std / min-max, Lomb-Scargle-free periodogram
(FFT of detrended, uniformly resampled data), and Allan deviation, plus
plots saved next to the input file.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_csv(path):
    """Return (t_seconds, y, ch2_or_None, y_is_mv).

    Two formats are understood:
    - Lab logger files: '# key,value' comment block, then named columns
      including elapsed_s and r_v (R in input-referred volts). Returns
      y = R in mV directly (y_is_mv = True); --sens is ignored.
    - Plain CSV [time, ch1_V(, ch2_V)]: returns y = CH1 volts
      (y_is_mv = False); main() converts via --sens.
    """
    header_cols = None
    rows = []
    with open(path, errors="replace") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = [p.strip() for p in line.replace(";", ",").split(",") if p.strip()]
            if not parts:
                continue
            if header_cols is None and "r_v" in [p.lower() for p in parts]:
                header_cols = [p.lower() for p in parts]
                continue
            rows.append(parts)
    if header_cols:
        it = header_cols.index("elapsed_s")
        ir = header_cols.index("r_v")
        t = np.array([float(r[it]) for r in rows])
        y = np.array([float(r[ir]) for r in rows]) * 1000.0    # -> mV
        return t - t[0], y, None, True
    rows = [r for r in rows if len(r) >= 2]
    # drop header rows (non-numeric second column)
    def _num(s):
        try:
            return float(s)
        except ValueError:
            return None

    data = [r for r in rows if _num(r[1]) is not None]
    if not data:
        sys.exit(f"no numeric data found in {path}")
    t_raw = [r[0] for r in data]
    ch1 = np.array([float(r[1]) for r in data])
    ch2 = np.array([float(r[2]) for r in data]) if len(data[0]) > 2 and _num(data[0][2]) is not None else None
    t0 = _num(t_raw[0])
    if t0 is not None:                       # numeric time column
        t = np.array([float(x) for x in t_raw])
        t -= t[0]
    else:                                    # HH:MM:SS or ISO timestamps
        import datetime as dt

        def parse(x):
            x = x.split()[-1]
            h, m, s = (float(v) for v in x.split(":"))
            return h * 3600 + m * 60 + s

        t = np.array([parse(x) for x in t_raw])
        t -= t[0]
        t[t < 0] += 86400                    # midnight rollover
    return t, ch1, ch2, False


def allan_deviation(y, dt, taus=None):
    """Non-overlapping Allan deviation of y sampled at interval dt."""
    n = len(y)
    if taus is None:
        taus = np.unique(np.round(np.logspace(0, np.log10(n // 3), 40)).astype(int))
        taus = taus[taus >= 1]
    out_tau, out_adev = [], []
    for m in taus:
        k = n // m
        if k < 3:
            break
        means = y[: k * m].reshape(k, m).mean(axis=1)
        adev = np.sqrt(0.5 * np.mean(np.diff(means) ** 2))
        out_tau.append(m * dt)
        out_adev.append(adev)
    return np.array(out_tau), np.array(out_adev)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--sens", type=float, default=100.0, help="lock-in sensitivity in mV (CH1 FS = 1 V)")
    ap.add_argument("--events", help="optional event-log file: 'HH:MM:SS label' per line")
    ap.add_argument("--t0", help="wall-clock HH:MM:SS of the first sample (to align events)")
    args = ap.parse_args()

    t, ch1, ch2, is_mv = load_csv(args.csv)
    r_mv = ch1 if is_mv else ch1 * args.sens
    dt = np.median(np.diff(t))
    print(f"{len(t)} samples, dt = {dt:.2f} s, duration = {t[-1]:.0f} s")
    print(f"R: mean {r_mv.mean():.2f} mV  std {r_mv.std():.2f} mV  "
          f"min {r_mv.min():.2f}  max {r_mv.max():.2f}")

    # ---- segments from event log ------------------------------------------
    segments = [(0.0, t[-1], "all")]
    if args.events:
        def clock(x):
            h, m, s = (float(v) for v in x.split(":"))
            return h * 3600 + m * 60 + s

        t0 = clock(args.t0) if args.t0 else None
        marks = []
        for line in open(args.events):
            parts = line.split(None, 1)
            if not parts:
                continue
            ts = clock(parts[0]) - (t0 if t0 is not None else clock(parts[0]))
            marks.append((ts, parts[1].strip() if len(parts) > 1 else ""))
        marks.sort()
        segments = []
        bounds = [0.0] + [m[0] for m in marks] + [t[-1]]
        labels = ["start"] + [m[1] for m in marks]
        for i, lab in enumerate(labels):
            segments.append((bounds[i], bounds[i + 1], lab))

    print("\nper-segment statistics (first/last 10% trimmed as settling):")
    for a, b, lab in segments:
        m = (t >= a) & (t < b)
        if m.sum() < 5:
            continue
        seg = r_mv[m]
        trim = max(1, len(seg) // 10)
        core = seg[trim:-trim] if len(seg) > 3 * trim else seg
        print(f"  {a:7.0f}-{b:7.0f} s  {lab[:30]:30s} "
              f"mid {np.median(core):7.2f} mV  band {core.min():.2f}-{core.max():.2f}  "
              f"std {core.std():.2f}")

    out = Path(args.csv).with_suffix("")

    # ---- time series plot --------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, r_mv, lw=0.7)
    for a, _b, lab in segments[1:]:
        ax.axvline(a, color="k", ls="--", lw=0.6)
        ax.text(a, ax.get_ylim()[1], lab[:15], rotation=90, va="top", fontsize=7)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("R (mV)")
    fig.tight_layout()
    fig.savefig(f"{out}_timeseries.png", dpi=150)

    # ---- periodogram (uniform resample + FFT) ------------------------------
    tu = np.arange(t[0], t[-1], dt)
    yu = np.interp(tu, t, r_mv)
    yu -= np.polyval(np.polyfit(tu, yu, 1), tu)      # detrend
    freq = np.fft.rfftfreq(len(yu), dt)
    psd = np.abs(np.fft.rfft(yu * np.hanning(len(yu)))) ** 2
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.loglog(freq[1:], psd[1:])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("PSD (arb.)")
    fig.tight_layout()
    fig.savefig(f"{out}_periodogram.png", dpi=150)
    fpk = freq[1:][np.argmax(psd[1:])]
    if fpk > 0:
        print(f"\ndominant fluctuation component: {fpk*1000:.2f} mHz  (period {1/fpk:.0f} s)")

    # ---- Allan deviation ---------------------------------------------------
    tau, adev = allan_deviation(yu, dt)
    if len(tau):
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.loglog(tau, adev, "o-", ms=3)
        ax.set_xlabel("averaging time τ (s)")
        ax.set_ylabel("Allan deviation (mV)")
        ax.grid(True, which="both", alpha=0.3)
        fig.tight_layout()
        fig.savefig(f"{out}_allan.png", dpi=150)
        i = np.argmin(adev)
        print(f"Allan minimum: {adev[i]:.3f} mV at τ = {tau[i]:.1f} s")
        print("(note: samples within one lock-in TC are correlated; ADEV below ~TC is optimistic)")

    print(f"\nplots: {out}_timeseries.png, {out}_periodogram.png, {out}_allan.png")


if __name__ == "__main__":
    main()
