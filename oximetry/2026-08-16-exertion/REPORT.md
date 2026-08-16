# Exertion session oximetry — 2026-08-16 17:32–18:42

Device: Checkme O2 Max (SN 603891), 2-second sampling.
Source: `Checkme O2 Max 603891_20260816173225.csv`.
Context (per `HEALTH-LOG-2026-08-13-W-running-and-oximeter-rules.md`): a
pre-registered prediction says exertion itself is low-risk and the **stop**
is the risk window (post-stop CO2 dip -> air hunger, expected 1–5 min after
stopping). Rule adopted: record, don't alarm. Note: 16.08 was designated
light-walking-only inside the 36 h fast scoring window (15–17.08).

## Session structure (from the data)

- **17:32–18:18**: sustained exertion, HR climbing 110 -> 130s, continuous
  motion. **18:18 peak 161 bpm** (hardest effort of the session).
- **18:18–18:33**: gradual taper, HR 146 -> 105 — a real cool-down, not a
  dead stop (matches the rule in note W).
- **~18:33**: stop. **18:33–18:42**: seated/still recovery.

## Results

| Metric | During exertion (~60 min) | Post-stop (0–9 min) |
|---|---|---|
| SpO2 | steady 95–97%, min 93% (single sample, high motion) | **rises** 95.4 -> 97.7% |
| Dips <93% | **none** | none |
| Pulse | mean 118–133 by block, peak 161 | 108 -> 80 within 2 min, ~71 by +6 min |

Post-stop minute-by-minute: HR 108 / 92 / 80 / 83 / 78 / 74 / 71 — and SpO2
96–98% throughout the predicted danger window.

## Reading against the pre-registered prediction (note W)

- "Falsified if air hunger appears during steady running" — no
  desaturation occurred during exertion; oxygenation was steady 95–97%.
- The predicted risk window (1–5 min post-stop) shows the *healthiest*
  numbers of the whole recording: SpO2 climbing to 97–98% while HR fell
  smoothly. Whatever the subjective experience was, **there was no
  objective desaturation at any point** — during exertion, at the stop, or
  after it.
- Heart-rate recovery ~28 bpm in the first minute and ~38 by two minutes
  is a normal-to-good autonomic recovery marker.
- Protocol note: sustained HR 120–160 for an hour is vigorous exertion,
  not light walking; per note W the scoring window (Sun 16.08) called for
  light walking only, with running resuming 18.08. Worth annotating in the
  fast's log so the endpoint isn't read as confounded silently.

## Files

- `Checkme O2 Max 603891_20260816173225.csv` — raw export
- `exertion-2026-08-16.png` — chart (app-style axes: SpO2 70–100)
