# SUEWS Hackathon — practice setup ✅

This is a **practice repository** for the [SUEWS Community Hackathon](https://community.suews.io/t/welcome-to-the-suews-community-hackathon-24-june/69)
(24 June 2026, UCL East). It exists to confirm the workflow end to end before the
day; the real challenge repository (with the city dataset and the heat-to-risk
bridge) is created at kickoff.

## Setup status

- ✅ Repo created from the [hackathon template](https://github.com/UMEP-dev/suews-hackathon-template).
- ✅ `supy` (SUEWS Python interface) installed in a fresh virtual environment.
- ✅ **SUEWS ran end to end** on the built-in sample data — see the
  [smoke-test notes](../analysis/SMOKE_TEST.md). It produced surface
  energy-balance fluxes and 2 m air temperature with plausible values.
- ✅ This GitHub Pages site is live.

> The sample run uses `supy`'s bundled example data, **not** the hackathon city
> dataset (revealed on the day). It only demonstrates that the pipeline works.

## On the day

The real page will tell the story:

- The question asked of SUEWS.
- How SUEWS was configured via the [suews-agent](https://github.com/UMEP-dev/suews-agent).
- The heat-hazard result and the socio-economic heat-risk indicator.
- Where the hazard-to-indicator bridge holds, and where it breaks.

## Citing SUEWS

- Järvi, L., Grimmond, C.S.B. & Christen, A. (2011). *Journal of Hydrology* 411, 219–237. https://doi.org/10.1016/j.jhydrol.2011.10.001
- Ward, H.C., Kotthaus, S., Järvi, L. & Grimmond, C.S.B. (2016). *Urban Climate* 18, 1–32. https://doi.org/10.1016/j.uclim.2016.05.001
