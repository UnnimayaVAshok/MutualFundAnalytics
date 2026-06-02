import requests
import pandas as pd
import os

# -----------------------------
# STEP 1: API URL
# -----------------------------
url = "https://api.mfapi.in/mf/125497"

print("Fetching data from API...")

# -----------------------------
# STEP 2: GET REQUEST
# -----------------------------
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully!")
else:
    print("Failed to fetch data:", response.status_code)
    exit()

# -----------------------------
# STEP 3: PARSE JSON
# -----------------------------
meta = data["meta"]
nav_data = data["data"]   # this is list of NAV history

# Convert NAV history into DataFrame
df = pd.DataFrame(nav_data)

# Add scheme details to each row (optional but useful)
df["scheme_code"] = meta["scheme_code"]
df["scheme_name"] = meta["scheme_name"]

# -----------------------------
# STEP 4: SAVE AS CSV
# -----------------------------
output_path = "data/raw/hdfc_top_100_nav.csv"

os.makedirs("data/raw", exist_ok=True)

df.to_csv(output_path, index=False)

print(f"CSV saved successfully at: {output_path}")

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}