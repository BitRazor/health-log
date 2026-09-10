# In-flight oximetry — 2026-08-11 19:07–21:22

Device: Checkme O2 Max (SN 603891), 2-second sampling.
Source: `Checkme O2 Max 603891_20260811190725.csv`.
Timeline (per user): recording starts on the ground; flight began ~19:50;
recording stopped mid-flight at 21:22.

## Segments

| Segment | Window | SpO2 mean / median / min | Time <94% | Time <90% | Time <88% | Pulse mean / median |
|---|---|---|---|---|---|---|
| Ground / boarding | 19:07–19:50 (43 min) | 95.8 / 96 / 90 | 3.9 min | 0 | 0 | 92 / 94 |
| Flight | 19:50–21:22 (92 min) | 92.6 / 92 / 88 | 68 min | 2.4 min | 0 | 77 / 77 |

- Climb profile: SpO2 held ~96% for the first ~15 min after takeoff, then
  drifted down as cabin altitude rose, stabilising at **91–92% from ~20:12**
  for the rest of the recording (classic cruise plateau).
- **Lowest values:** absolute min 88% (momentary, 20:32); worst rolling
  60 s mean 89.3% at 20:32. Never below 88%, and time under 90% totalled
  only 2.4 min out of 92.
- **Pulse fell in flight**: ~92 bpm during boarding/walking to a settled
  ~72–78 bpm seated at cruise (max in-flight 100, no tachycardia).

## Interpretation notes (not a diagnosis)

- Airliner cabins are pressurised to an equivalent altitude of roughly
  1800–2400 m. At that altitude healthy adults commonly run **SpO2 90–94%**;
  a drop from 96% at sea level to a 92% cruise median with brief dips to
  88–89% is the *expected, normal* response to cabin altitude — not a sign
  of a breathing or lung problem.
- The reassuring details: no sustained desaturation (nothing below 88%,
  <90% only 2.4 min total), stable plateau rather than progressive decline,
  and a *low, calm* pulse throughout the flight.
- Relevance to the air-hunger question: mild altitude hypoxia raises
  respiratory drive, so a person sensitised to that signal will often feel
  air hunger in flight even though saturation is in the normal-for-altitude
  band. The data shows the sensation, if present, was not matched by any
  abnormal desaturation.

## Files

- `Checkme O2 Max 603891_20260811190725.csv` — raw export
- `analyze_flight.py` — segmentation + stats
- `plot_flight.py` → `flight-2026-08-11.png` — annotated chart
