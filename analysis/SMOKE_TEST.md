# SUEWS toolchain smoke test (practice setup)

This documents the end-to-end check run while setting up the practice repo, to
confirm the SUEWS toolchain works before the hackathon (24 June 2026).

## What was run

- **Package:** `supy` 2026.6.5 (the SUEWS Python interface), installed into a
  fresh `venv` on Python 3.14.6.
- **Data:** `supy`'s **built-in sample dataset** (Kc 2012, Kings College London
  forcing) via `SUEWSSimulation.from_sample_data()`.
  This is **not** the hackathon city dataset — that is loaded at kickoff on
  24 June. The sample run only proves the pipeline works end to end.
- **Window:** first 7 days of 2012 (a short slice to keep the test small/fast).
- **Script:** [`example_run.py`](example_run.py) · **Captured output:** [`example_run_output.txt`](example_run_output.txt)

## How to reproduce

```bash
# from the repo root
python3 -m venv .venv          # .venv is gitignored
.venv/bin/python -m pip install supy
.venv/bin/python analysis/example_run.py
```

## Result

`SUEWS end-to-end smoke test PASSED` — the model produced surface energy-balance
fluxes (QH, QE, QS), 2 m air temperature (T2) and incoming shortwave (Kdown),
with plausible daily-mean T2 of ~6–11 °C for a London January. Output shape
`(2303, 1081)`.

## Note on the suews-agent

On the day, runs are driven through the [suews-agent](https://github.com/UMEP-dev/suews-agent),
a Claude Code / Codex plugin that wraps SUEWS (it launches the `suews-mcp` server
via `uvx`). This first check exercised the underlying engine (`supy`) directly;
the agent layer itself has since been verified end to end (init → validate →
inspect → run → summarise) — see [`agent_smoke/AGENT_RUN.md`](agent_smoke/AGENT_RUN.md).

## Citing SUEWS

- Järvi, L., Grimmond, C.S.B. & Christen, A. (2011). *J. Hydrology* 411, 219–237.
  https://doi.org/10.1016/j.jhydrol.2011.10.001
- Ward, H.C., Kotthaus, S., Järvi, L. & Grimmond, C.S.B. (2016). *Urban Climate*
  18, 1–32. https://doi.org/10.1016/j.uclim.2016.05.001
