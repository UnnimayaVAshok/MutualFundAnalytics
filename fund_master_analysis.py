import pandas as pd

# -----------------------------
# LOAD DATASETS
# -----------------------------
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/hdfc_top_100_nav.csv")

df = fund_master  # cleaner reference

# -----------------------------
# CHECK STRUCTURE
# -----------------------------
print(fund_master.columns)

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

# -----------------------------
# AMFI CODE VALIDATION
# -----------------------------
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["scheme_code"])

missing_in_nav = master_codes - nav_codes
missing_in_master = nav_codes - master_codes

print("\nIn Master but NOT in NAV:", len(missing_in_nav))
print("In NAV but NOT in Master:", len(missing_in_master))

# -----------------------------
# DATA QUALITY SUMMARY
# -----------------------------
print("\nDATA QUALITY SUMMARY")
print("----------------------")
print("Total Master Codes:", len(master_codes))
print("Total NAV Codes:", len(nav_codes))
print("Missing in NAV:", len(missing_in_nav))
print("Missing in Master:", len(missing_in_master))