import pandas as pd
from sqlalchemy import create_engine

#creating sql connection
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

print("Database connected")

#loading cleaned nav dataset
nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav table loaded")

#loading transaction dataset
transactions_df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

transactions_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions table loaded")

#loading performance dataset
performance_df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance table loaded")

print(nav_df.shape)
print(transactions_df.shape)
print(performance_df.shape)

