# Mutual Fund Analytics Capstone Project

## Project Overview

This project focuses on building a complete Mutual Fund Analytics pipeline using Python, Pandas, SQLite, SQL, and data visualization tools.

The project includes:

* Data ingestion
* Data cleaning
* SQLite database creation
* ETL pipeline
* Exploratory Data Analysis (EDA)
* Performance analytics
* Dashboard development

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook

## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Deliverables

* Cleaned datasets
* SQLite database
* SQL schema
* Analytical SQL queries
* EDA notebooks
* Dashboard
* Final report and presentation

## Dataset Descriptions

### NAV History Dataset

Contains historical Net Asset Value (NAV) records used for return calculations, performance analysis, and risk metrics.

### AUM Dataset

Contains Assets Under Management (AUM) information used for industry and fund house analysis.

### Scheme Performance Dataset

Contains return and risk measures including Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Drawdown metrics.

### Investor Transactions Dataset

Contains SIP, Lumpsum, and Redemption transactions used for investor behavior analysis.

---

## Setup Instructions

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn plotly sqlalchemy requests
```

---

## Running the ETL Pipeline

Run the master pipeline script:

```bash
python run_pipeline.py
```

This executes:

* data_ingestion.py
* fetch_nav.py
* fund_master_analysis.py

---

## Running the Fund Recommender

```bash
python recommender.py
```

Enter one of:

* Low
* Moderate
* High

The script returns the top recommended funds based on Sharpe Ratio and risk category.

---

## Dashboard

Open the Power BI dashboard file:

```text
bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

Dashboard Pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends
