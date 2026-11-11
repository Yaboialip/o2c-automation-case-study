"""Simulated O2C data for the PT Maju Distribusi Nusantara case study.
ALL DATA IS SYNTHETIC. Parameters are assumptions chosen to illustrate the KPI method, not real measurements.
Run: python generate_data.py  (needs numpy, pandas, matplotlib)"""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)          # fixed seed: reproducible
N = 5000                                  # orders over 90 days

base = pd.DataFrame({
    "order_id": np.arange(1, N + 1),
    "order_ts": pd.Timestamp("2026-01-05") + pd.to_timedelta(rng.integers(0, 90 * 24 * 60, N), unit="m"),
    "customer_id": rng.integers(1, 351, N),
    "lines": rng.integers(1, 8, N),
})
PARAMS = {  # median hours, sigma, oversell prob, error prob, invoice delay median hours, sigma
    "AS_IS": dict(med=20.0, sigma=0.6, oversell=0.09,  error=0.06,  inv_med=32.0, inv_sigma=0.5),
    "TO_BE": dict(med=1.2,  sigma=0.5, oversell=0.008, error=0.008, inv_med=0.1,  inv_sigma=0.5),
}
def simulate(df, scenario):
    p = PARAMS[scenario]; out = df.copy()
    out["processing_hours"] = rng.lognormal(np.log(p["med"]), p["sigma"], len(out))
    out["oversold"] = rng.random(len(out)) < p["oversell"]
    out["data_error"] = rng.random(len(out)) < p["error"]
    out["invoice_delay_hours"] = rng.lognormal(np.log(p["inv_med"]), p["inv_sigma"], len(out))
    out["scenario"] = scenario
    out["week"] = out["order_ts"].dt.isocalendar().week.astype(int)
    return out
result = pd.concat([simulate(base, "AS_IS"), simulate(base, "TO_BE")], ignore_index=True)
result.to_csv("o2c_simulated_orders.csv", index=False)

summary = result.groupby("scenario").agg(
    orders=("order_id", "count"),
    avg_processing_hours=("processing_hours", "mean"),
    p90_processing_hours=("processing_hours", lambda s: s.quantile(0.9)),
    oversell_rate=("oversold", "mean"),
    error_rate=("data_error", "mean"),
    avg_invoice_delay_hours=("invoice_delay_hours", "mean"),
).round(4)
summary["avg_invoice_delay_minutes"] = (result.groupby("scenario")["invoice_delay_hours"].mean() * 60).round(1)  # from unrounded mean
summary.to_csv("kpi_summary.csv")
print(summary.T)

colors = {"AS_IS": "#b45309", "TO_BE": "#2f5d8a"}
fig, ax = plt.subplots(1, 4, figsize=(15, 3.8))
for a, (col, ttl, tgt, f) in zip(ax, [("avg_processing_hours", "Avg order processing (h)", 2, 1),
        ("oversell_rate", "Overselling rate (%)", 1, 100), ("error_rate", "Order error rate (%)", 1, 100),
        ("avg_invoice_delay_minutes", "Invoice lead time (min)", 15, 1)]):
    vals = [summary.loc[s, col] * f for s in ("AS_IS", "TO_BE")]
    a.bar(["AS-IS", "TO-BE"], vals, color=[colors["AS_IS"], colors["TO_BE"]])
    a.axhline(tgt, color="gray", ls="--", lw=1); a.set_title(ttl, fontsize=10)
    for i, v in enumerate(vals): a.text(i, v, f"{v:.1f}", ha="center", va="bottom", fontsize=9)
fig.suptitle("Simulated KPI comparison (dashed line = target). Synthetic data.", fontsize=10)
fig.tight_layout(); fig.savefig("kpi_comparison.png", dpi=150); plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 3.8))
for s in ("AS_IS", "TO_BE"):
    ax.hist(result.loc[result.scenario == s, "processing_hours"].clip(upper=72), bins=60, alpha=.65,
            label=s.replace("_", "-"), color=colors[s])
ax.set_xlabel("Order processing time (hours, capped at 72)"); ax.set_ylabel("Orders"); ax.legend()
ax.set_title("Processing time distribution (simulated)", fontsize=10)
fig.tight_layout(); fig.savefig("processing_time_distribution.png", dpi=150)
