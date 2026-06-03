# Data Dictionary

## fact_nav

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Unique mutual fund identifier |
| date      | DATE      | NAV date                      |
| nav       | FLOAT     | Net Asset Value               |

---

## fact_transactions

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Mutual fund scheme code    |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr         | FLOAT     | Investment amount          |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age category      |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | FLOAT     | Annual income in lakhs     |
| payment_mode       | TEXT      | Mode of payment            |
| kyc_status         | TEXT      | Investor KYC status        |

---

## fact_performance

| Column             | Data Type | Description              |
| ------------------ | --------- | ------------------------ |
| amfi_code          | INTEGER   | Mutual fund scheme code  |
| scheme_name        | TEXT      | Fund scheme name         |
| fund_house         | TEXT      | Asset management company |
| category           | TEXT      | Fund category            |
| plan               | TEXT      | Direct/Regular           |
| return_1yr_pct     | FLOAT     | 1-year return percentage |
| return_3yr_pct     | FLOAT     | 3-year return percentage |
| return_5yr_pct     | FLOAT     | 5-year return percentage |
| benchmark_3yr_pct  | FLOAT     | Benchmark return         |
| alpha              | FLOAT     | Alpha metric             |
| beta               | FLOAT     | Beta metric              |
| sharpe_ratio       | FLOAT     | Risk-adjusted return     |
| sortino_ratio      | FLOAT     | Downside risk ratio      |
| std_dev_ann_pct    | FLOAT     | Annualized volatility    |
| max_drawdown_pct   | FLOAT     | Maximum loss percentage  |
| aum_crore          | FLOAT     | Assets under management  |
| expense_ratio_pct  | FLOAT     | Expense ratio            |
| morningstar_rating | INTEGER   | Fund rating              |
| risk_grade         | TEXT      | Risk classification      |
