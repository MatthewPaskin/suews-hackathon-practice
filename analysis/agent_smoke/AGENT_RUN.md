# suews-agent end-to-end test run (practice)

This closes the one gap left by [`../SMOKE_TEST.md`](../SMOKE_TEST.md): that
earlier check exercised the engine (`supy`) **directly**, not through the
**suews-agent**. Here the run is driven entirely through the agent's
`suews-mcp` server — the same layer used on the day (24 June 2026).

## Setup verified

- Plugin `suews@suews` installed (project scope) from marketplace
  `UMEP-dev/suews-agent`; declared in [`../../.claude/settings.json`](../../.claude/settings.json).
- `suews-mcp` **2026.6.5** launches via `uvx --from git+https://github.com/UMEP-dev/SUEWS.git#subdirectory=mcp suews-mcp`
  and exposes **14 tools** (init/validate/inspect/summarise/compare/diagnose,
  schema & docs search, versioned knowledge pack).

## Agent workflow run (in order)

| Step | Tool | Result |
|------|------|--------|
| 1 | `init_case` (template `simple-urban`) | scaffolded `sample_config.yml` + `Kc_2012_data_60.txt` forcing |
| 2 | `validate_config` | `is_valid: true`, 0 errors |
| 3 | `inspect_config` | site **KCL** (51.51, −0.12), surface fractions sum to 1.0, 24-col forcing |
| 4 | `suews run sample_config.yml` (CLI) | full year 2012 ran cleanly → `Output/KCL1_2012_SUEWS_60.txt` |
| 5 | `summarise_run` | 8784 hourly steps, **0 % NaN** on all variables |

## Result — plausible for London 2012

| Var | mean | min | max |
|-----|------|-----|-----|
| T2 (2 m air temp, °C) | 11.91 | −5.24 | 30.40 |
| Tsurf (°C) | 12.60 | −5.58 | 36.15 |
| RH2 (%) | 69.33 | 18.75 | 98.16 |
| QN (net radiation, W m⁻²) | 44.76 | −83.80 | 646.98 |
| QH (sensible heat, W m⁻²) | 88.76 | −40.82 | 339.70 |
| QE (latent heat, W m⁻²) | 27.58 | 1.70 | 195.34 |
| QF (anthropogenic heat, W m⁻²) | 84.52 | 31.15 | 157.90 |

This is the **built-in sample dataset (Kc 2012, Kings College London)**, *not*
the hackathon city — that is released at kickoff. The run only proves the
agent-driven pipeline works end to end.

## Reproduce

```bash
# 1. launch agent / MCP server is handled by your Claude Code session, or directly:
uvx --from "git+https://github.com/UMEP-dev/SUEWS.git#subdirectory=mcp" suews-mcp   # MCP stdio server

# 2. the run step (CLI from the same supy install):
cd analysis/agent_smoke
../../.venv/bin/suews run sample_config.yml      # writes Output/
```

The bulky raw `Output/` (9.3 MB) is gitignored; this note captures the summary.
