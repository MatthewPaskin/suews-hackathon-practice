"""
SUEWS end-to-end smoke test for the hackathon practice setup.

Uses supy's bundled sample data (Kc 2012, Kings College London forcing) and the
modern object-oriented SUEWSSimulation interface. Runs a short period to confirm
the toolchain works end to end before the hackathon. NOT the city dataset — that
is loaded at kickoff on 24 June 2026.

Cite SUEWS:
  Jarvi et al. (2011), J. Hydrology 411:219-237, doi:10.1016/j.jhydrol.2011.10.001
  Ward et al. (2016), Urban Climate 18:1-32, doi:10.1016/j.uclim.2016.05.001
"""
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from supy.suews_sim import SUEWSSimulation

sim = SUEWSSimulation.from_sample_data()

# Inspect the sample forcing window so we can pick a short, valid slice.
forcing = sim.forcing
print("supy sample forcing index range:")
print("  start:", forcing.index.min())
print("  end:  ", forcing.index.max())
print("  rows: ", len(forcing))

# Run a short window (first 7 days) to keep the smoke test small and fast.
start = forcing.index.min()
end = start + (forcing.index[1] - forcing.index[0]) * (288 * 7)  # ~7 days at 5-min steps

print(f"\nRunning SUEWS from {start} to {end} ...")
out = sim.run(start_date=str(start.date()), end_date=str(end.date()))

results = out.df  # SUEWSOutput -> raw DataFrame (non-deprecated path)
print("\nRun complete. Results shape:", results.shape)

# Output columns are a MultiIndex (group, variable); grab the SUEWS group.
suews = results["SUEWS"] if "SUEWS" in results.columns.get_level_values(0) else results
cols = [c for c in ["QH", "QE", "QS", "T2", "Kdown"] if c in suews.columns]
print("Key SUEWS output variables (first 3 timesteps):")
print(suews[cols].head(3).to_string())

# Index is a MultiIndex (grid, datetime); drop grid for a clean daily resample.
suews_t = suews.reset_index(level="grid", drop=True) if "grid" in suews.index.names else suews
print("\nDaily mean air temperature T2 (degC):")
if "T2" in suews_t.columns:
    print(suews_t["T2"].resample("1D").mean().round(2).to_string())

print("\nSUEWS end-to-end smoke test PASSED.")
