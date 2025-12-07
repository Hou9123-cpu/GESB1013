import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv("filtered_data.csv")

print("\n=== 描述性统计（各国均值） ===")
print(df.groupby("geo")["ag_con_fert_pt_zs"].describe())

plt.figure(figsize=(12, 6))
for c in df["geo"].unique():
    sub = df[df["geo"] == c]
    plt.plot(sub["time"], sub["ag_con_fert_pt_zs"], label=c)

plt.title("Fertilizer Use Trend (1980–2020)")
plt.xlabel("Year")
plt.ylabel("kg/ha")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("trend.png")
plt.show()

print("\n=== 时间相关性（每国） ===")
for c in df["geo"].unique():
    sub = df[df["geo"] == c]
    corr = stats.pearsonr(sub["time"], sub["ag_con_fert_pt_zs"])
    print(f"{c}: r={corr[0]:.3f}, p={corr[1]:.4f}")

print("\n=== 线性回归（时间 → 化肥使用） ===")
for c in df["geo"].unique():
    sub = df[df["geo"] == c]
    model = smf.ols("ag_con_fert_pt_zs ~ time", data=sub).fit()
    print(f"\n--- {c} ---")
    print(model.summary())

print("\n=== ANOVA：国家间均值差异 ===")
anova_model = smf.ols("ag_con_fert_pt_zs ~ C(geo)", data=df).fit()
anova_table = sm.stats.anova_lm(anova_model)
print(anova_table)