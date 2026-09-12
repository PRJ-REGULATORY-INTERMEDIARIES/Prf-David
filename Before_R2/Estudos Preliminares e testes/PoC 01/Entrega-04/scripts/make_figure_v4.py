"""Create the descriptive five-act screening figure used by the report."""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
acts = ["CSRD", "Ecolabel", "Climate", "ETS", "Taxonomy"]
hits = [559, 94, 61, 365, 13]
fig, ax = plt.subplots(figsize=(9, 4.7), dpi=180)
bars = ax.bar(acts, hits, color="#3b82a0")
ax.set_title("Stage A1 screening hits by act", fontsize=14, weight="bold", color="#203040")
ax.set_ylabel("Screening hits")
ax.set_ylim(0, 600)
ax.grid(axis="y", alpha=0.2)
ax.set_axisbelow(True)
for bar, value in zip(bars, hits):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 10, str(value), ha="center", weight="bold")
fig.text(0.5, 0.01, "Descriptive screening distribution; not an estimate of intermediary prevalence.", ha="center", fontsize=8)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(ROOT / "figures" / "screening_distribution_v4.png", bbox_inches="tight")
plt.close(fig)
print(ROOT / "figures" / "screening_distribution_v4.png")
