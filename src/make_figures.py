from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

ret = pd.read_csv(RESULTS / "return_regression.csv")
plot = ret[ret.variable.isin(["Cloud Cover", "Rainfall", "Temperature", "Sunlight Hours"])]
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.bar(plot.variable, plot.coefficient)
ax.axhline(0, linewidth=0.8)
ax.set_ylabel("Reported coefficient")
ax.set_title("Weather Variables and Daily Excess Returns")
ax.tick_params(axis="x", rotation=20)
fig.tight_layout()
fig.savefig(FIGURES / "return_regression.png", dpi=180)
plt.close(fig)

sub = pd.read_csv(RESULTS / "subperiod_results.csv")
fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.bar(sub.period, sub.cloud_coefficient)
ax.axhline(0, linewidth=0.8)
ax.set_ylabel("Cloud-cover coefficient")
ax.set_title("Cloud-Cover Effect by Subperiod")
fig.tight_layout()
fig.savefig(FIGURES / "subperiod_comparison.png", dpi=180)
plt.close(fig)
