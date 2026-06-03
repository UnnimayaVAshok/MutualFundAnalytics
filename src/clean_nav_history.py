import pandas as pd

df = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

df['date'] = pd.to_datetime(
    df['date'],
    errors='coerce'
) 

df = df.sort_values(
    ['amfi_code', 'date']
)

df['nav'] = df.groupby(
    'amfi_code'
)['nav'].ffill()

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df[df['nav'] <= 0])

df = df[df['nav'] > 0]

print(df.head())
print(df.shape)
print(df.dtypes)

df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("NAV cleaning completed")