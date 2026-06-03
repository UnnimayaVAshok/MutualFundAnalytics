import pandas as pd

df = pd.read_csv(
"data/raw/07_scheme_performance.csv"
)

print(df.head())
print(df.shape)
print(df.dtypes)

# Convert return columns to numeric
return_cols = [
'return_1yr_pct',
'return_3yr_pct',
'return_5yr_pct'
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

# Detect anomalies in returns
anomalies = df[
(df['return_1yr_pct'] > 200) |
(df['return_1yr_pct'] < -100)
]

print("Anomalies:")
print(anomalies)

# Validate expense ratio
invalid_expense = df[
(df['expense_ratio_pct'] < 0.1) |
(df['expense_ratio_pct'] > 2.5)
]

print("Invalid expense ratios:")
print(invalid_expense)

# Save cleaned dataset
df.to_csv(
"data/processed/07_scheme_performance_cleaned.csv",
index=False
)

print("Performance cleaning completed")
