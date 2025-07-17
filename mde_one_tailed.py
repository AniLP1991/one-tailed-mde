import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

# ── EXPERIMENT‑LEVEL CONSTANTS (rarely change) ──────────────────
alpha = 0.05   # significance level (one‑tailed)
beta  = 0.20   # 1 – power  (0.20 ⇒ 80 % power)

# ── EDIT THESE THREE FOR *EACH* NEW TEST ─────────────────────────
cr      = 0.20   # baseline conversion rate of the primary metric
traffic = 8000   # weekly visitors to the test experience
split   = 0.50   # proportion of traffic per variant (e.g. 0.5 for A/B)

# ── DO NOT EDIT BELOW THIS LINE UNLESS YOU’RE CHANGING THE LOGIC ─
n = traffic * split
z_alpha = norm.ppf(1 - alpha)        # ≈ 1.645 for α = 0.05 (1‑tailed)
z_beta  = norm.ppf(1 - beta)         # ≈ 0.840 for 80 % power
se      = np.sqrt(2 * cr * (1 - cr) / n)
mde_pp  = (z_alpha + z_beta) * se * 100

print(f"One‑tailed MDE for a single week: {mde_pp:.2f}%")

# ── MDE BY WEEK TABLE ────────────────────────────────────────────
rows, max_weeks = [], 10
for week in range(1, max_weeks + 1):
    n_var = traffic * split * week
    se_w  = np.sqrt(2 * cr * (1 - cr) / n_var)
    mde_w = (z_alpha + z_beta) * se_w
    rows.append(
        {
            "Week": week,
            "Total Sample Size": int(traffic * week),
            "Per Variant": int(n_var),
            "MDE (prop)": round(mde_w, 4),
            "MDE (pp)":   round(mde_w * 100, 2),
        }
    )

df = pd.DataFrame(rows)
print("\nMDE progression by week:\n")
print(df.to_string(index=False))

# ── QUICK VISUAL ─────────────────────────────────────────────────
plt.figure(figsize=(6, 4))
plt.plot(df["Week"], df["MDE (pp)"], marker="o")
plt.xlabel("Weeks")
plt.ylabel("MDE (%)")
plt.title("Decreasing MDE over 10 Weeks (One‑tailed Test)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
