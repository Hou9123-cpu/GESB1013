import pandas as pd

df = pd.read_csv("ddf--datapoints--ag_con_fert_pt_zs--by--geo--time.csv")


countries = ["chn", "jpn", "usa", "gbr", "deu", "ind", "bra", "zaf", "aus"]

start_year = 1980
end_year = 2020

df_filtered = df[
    (df["geo"].isin(countries)) &
    (df["time"] >= start_year) &
    (df["time"] <= end_year)
]

output_file = f"fertilizer_9countries_{start_year}_{end_year}.csv"
df_filtered.to_csv(output_file, index=False)

print("已生成文件：", output_file)
print("最终数据形状：", df_filtered.shape)
print(df_filtered.head())