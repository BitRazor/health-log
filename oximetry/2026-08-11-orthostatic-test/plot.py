#!/usr/bin/env python3
"""Chart for the 2026-08-11 orthostatic test."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from analyze import load, CSV_FILE, SETTLE_CUT_S, TRANSITION_CUT_S
from datetime import timedelta

rows = load(CSV_FILE)
t0 = rows[0][0]
t_settle = t0 + timedelta(seconds=SETTLE_CUT_S)
t_up = next(r[0] for r in rows if r[0].strftime("%H:%M:%S") == "07:00:14")
t_std = t_up + timedelta(seconds=TRANSITION_CUT_S)

t = [r[0] for r in rows]
spo2 = [r[1] for r in rows]
hr = [r[2] for r in rows]

fig, ax = plt.subplots(figsize=(12, 5.5))
ax.axvspan(t0, t_settle, color="#bbbbbb", alpha=0.45, label="excluded (cuts)")
ax.axvspan(t_up, t_std, color="#bbbbbb", alpha=0.45)
ax.axvspan(t_settle, t_up, color="#4c72b0", alpha=0.10)
ax.axvspan(t_std, t[-1], color="#dd8452", alpha=0.10)

ax.plot(t, hr, color="#c44e52", lw=1.4, label="Pulse (bpm)")
ax.plot(t, spo2, color="#4c72b0", lw=1.1, label="SpO2 (%)")

ax.axhline(55, color="#c44e52", ls=":", lw=1)
ax.axhline(89, color="#c44e52", ls="--", lw=1)
ax.annotate("supine median 55 bpm", (t_settle, 55), xytext=(0, -14),
            textcoords="offset points", fontsize=9, color="#883333")
ax.annotate("standing median 89 bpm  (delta +34)", (t_settle, 89),
            xytext=(0, 6), textcoords="offset points", fontsize=9,
            color="#883333")
ax.annotate("stood up 07:00:22", (t_up, 100), xytext=(-95, 12),
            textcoords="offset points", fontsize=9,
            arrowprops=dict(arrowstyle="->", lw=1))

ax.text(t_settle + timedelta(seconds=120), 47, "LYING DOWN (8.5 min)",
        fontsize=10, color="#33507a", weight="bold")
ax.text(t_std + timedelta(seconds=100), 47, "STANDING (9.4 min)",
        fontsize=10, color="#9a5320", weight="bold")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.set_ylim(44, 104)
ax.set_ylabel("bpm / %")
ax.set_title("Checkme O2 Max — orthostatic test 2026-08-11 06:51 "
             "(first 30 s and 30 s stand-up transition excluded)")
ax.legend(loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("orthostatic-2026-08-11.png", dpi=140)
print("saved orthostatic-2026-08-11.png")
