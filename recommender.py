"""
Bluestock Mutual Fund Analytics Capstone

Purpose:
Recommend the top mutual funds based on the investor's
risk appetite using Sharpe Ratio rankings.

Author: Unnimaya V Ashok
Date: June 2026
"""

import pandas as pd

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)


risk = input(
    "Enter risk appetite (Low/Moderate/High): "
)

recommend = perf_df[
    perf_df['risk_grade'] == risk
]

recommend = recommend.sort_values(
    'sharpe_ratio',
    ascending=False
).head(3)

print(
    recommend[
        ['fund_house', 'sharpe_ratio']
    ]
)