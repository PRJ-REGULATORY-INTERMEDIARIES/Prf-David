"""Create the six analytical figures required by the v4 report."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)
BLUE = "#2f6f8f"
PALE = "#e7f1f5"
INK = "#203040"
GREEN = "#6d9e78"
GOLD = "#d3a64a"


def box(ax, x, y, w, h, label, color=PALE, fontsize=10):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02",
                           linewidth=1.2, edgecolor=BLUE, facecolor=color)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            color=INK, fontsize=fontsize, wrap=True)


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=12, linewidth=1.2, color=BLUE))


def save(fig, name):
    fig.savefig(FIGURES / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


def fig1():
    fig, ax = plt.subplots(figsize=(8.8, 10.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis("off")
    labels = [
        "REGULATORY CONTEXT", "REGULATORY ARCHITECTURE", "R - I - T RELATIONSHIP",
        "REGULATORY INTERMEDIATION\nActors + Mechanisms + Strategies",
        "INTERMEDIARY INSTITUTIONAL DESIGN", "AUTONOMY / ACCOUNTABILITY\nINDICATORS",
        "FAILURE RISKS / SAFEGUARDS", "[future empirical analysis]\nEffectiveness / Legitimacy / Trust",
        "[future aggregate analysis]\nMonocentric <-> Polycentric",
    ]
    ys = [10.9, 9.55, 8.2, 6.65, 5.3, 3.95, 2.6, 1.25, 0.0]
    for i, (label, y) in enumerate(zip(labels, ys)):
        box(ax, 1.1, y, 7.8, 0.85, label, color="#f2f7f8" if i < 7 else "#fff6df")
        if i < len(labels) - 1:
            arrow(ax, 5, y, 5, ys[i + 1] + 0.85)
    ax.set_title("Figure 1. Conceptual framework", color=INK, weight="bold", pad=14)
    save(fig, "fig1_conceptual_framework_v4.png")


def fig2():
    fig, ax = plt.subplots(figsize=(12, 4.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 4); ax.axis("off")
    labels = ["EUR-Lex\nCELEX manifest", "A1 + A2\nscreening", "Candidate\npool", "B1\narchitecture", "B2\nR-I-T test", "Human\nadjudication", "C + D\nattributes / validation", "Authoritative\ndata"]
    xs = [0.2, 1.7, 3.2, 4.7, 6.2, 7.7, 9.2, 10.7]
    for x, label in zip(xs, labels):
        box(ax, x, 1.4, 1.25, 1.15, label, color="#f2f7f8", fontsize=9)
    for x in xs[:-1]:
        arrow(ax, x + 1.25, 1.98, x + 1.5, 1.98)
    ax.text(6, 3.25, "AI proposals are logged and reviewed; they never write directly to authoritative tables.",
            ha="center", color=INK, fontsize=10, style="italic")
    ax.text(6, 0.5, "SPARQL / Cellar solves retrieval, not population definition.", ha="center", color=INK, fontsize=9)
    ax.set_title("Figure 2. AI-assisted evidence pipeline", color=INK, weight="bold", pad=12)
    save(fig, "fig2_ai_pipeline_v4.png")


def fig3():
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    cats = ["Lexical only\n(observed sample)", "Both", "Semantic AI only", "Human discovery"]
    vals = [20, 0, 0, 0]
    bars = ax.bar(cats, vals, color=[BLUE, "#9db8c5", GOLD, GREEN])
    ax.set_ylim(0, 24); ax.set_ylabel("Units")
    ax.set_title("Figure 3. Candidate-discovery channels", color=INK, weight="bold")
    ax.grid(axis="y", alpha=0.2); ax.set_axisbelow(True)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.7, str(val), ha="center", weight="bold")
    fig.text(0.5, 0.01, "Substantive A2 was not executed; overlap and AI-only discovery are NOT MEASURED, not zero findings.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, "fig3_discovery_overlap_v4.png")


def fig4():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    for ax in axes:
        ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax = axes[0]
    box(ax, 0.4, 2.0, 2.2, 1.0, "Rule-maker /\nregulator R")
    box(ax, 3.8, 2.0, 2.2, 1.0, "Intermediary I\nassurance")
    box(ax, 7.4, 2.0, 2.2, 1.0, "Target T\nundertaking")
    arrow(ax, 2.6, 2.5, 3.8, 2.5); arrow(ax, 6.0, 2.5, 7.4, 2.5)
    ax.text(5, 1.2, "mediating function: assurance / audit", ha="center", color=INK, fontsize=9)
    ax.set_title("Direct R-I-T", color=INK, weight="bold")
    ax = axes[1]
    box(ax, 0.3, 3.2, 2.1, 0.9, "Regulator R")
    box(ax, 3.1, 3.2, 2.1, 0.9, "I1\ngroup auditor")
    box(ax, 6.0, 3.2, 2.1, 0.9, "I2\nassurance provider")
    box(ax, 3.1, 0.8, 2.1, 0.9, "Target T\nundertaking")
    arrow(ax, 2.4, 3.65, 3.1, 3.65); arrow(ax, 5.2, 3.65, 6.0, 3.65)
    arrow(ax, 7.05, 3.2, 4.2, 1.7); arrow(ax, 4.15, 3.2, 4.15, 1.7)
    ax.text(5, 0.25, "architecture first; roles remain relationship-specific", ha="center", color=INK, fontsize=8)
    ax.set_title("Nested / chained architecture", color=INK, weight="bold")
    fig.suptitle("Figure 4. R-I-T architecture examples", color=INK, weight="bold")
    save(fig, "fig4_rit_architecture_v4.png")


def fig5():
    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 5); ax.axis("off")
    box(ax, 0.3, 2.5, 2.1, 1.0, "Accreditation\nframework")
    box(ax, 3.0, 2.5, 2.1, 1.0, "National\naccreditation body")
    box(ax, 5.7, 2.5, 2.1, 1.0, "Verifier")
    box(ax, 8.4, 2.5, 2.1, 1.0, "Operator")
    for x in (2.4, 5.1, 7.8):
        arrow(ax, x, 3.0, x + 0.6, 3.0)
    ax.text(1.35, 1.55, "L2", ha="center", weight="bold", color=BLUE)
    ax.text(4.05, 1.55, "L2", ha="center", weight="bold", color=BLUE)
    ax.text(6.75, 1.55, "L1", ha="center", weight="bold", color=BLUE)
    ax.text(6, 0.6, "Parent relationship and evidence are required before coding meta-regulatory relation.",
            ha="center", color=INK, fontsize=9)
    ax.set_title("Figure 5. Nested intermediation and governance chain", color=INK, weight="bold", pad=12)
    save(fig, "fig5_nested_intermediation_v4.png")


def fig6():
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 5); ax.axis("off")
    labels = ["Legal text +\ncontext package", "AI proposal\n(strict schema)", "Human\nadjudication", "Independent\nvalidation", "Promotion only if\napproved"]
    xs = [0.3, 2.7, 5.1, 7.5, 9.9]
    colors = ["#f2f7f8", "#fff6df", "#e9f3e9", "#e9f3e9", "#f2f7f8"]
    for x, label, color in zip(xs, labels, colors):
        box(ax, x, 1.8, 1.8, 1.15, label, color=color, fontsize=9)
    for x in xs[:-1]:
        arrow(ax, x + 1.8, 2.38, x + 2.4, 2.38)
    ax.text(6, 4.05, "Disagreement, missing evidence and context gaps route back to review.",
            ha="center", color=INK, fontsize=10, style="italic")
    ax.text(6, 0.55, "Researcher adjudication is not a second-coder reliability estimate.",
            ha="center", color=INK, fontsize=9)
    ax.set_title("Figure 6. Human-in-the-loop validation architecture", color=INK, weight="bold", pad=12)
    save(fig, "fig6_human_validation_v4.png")


if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6()
    print(f"Wrote six figures to {FIGURES}")
