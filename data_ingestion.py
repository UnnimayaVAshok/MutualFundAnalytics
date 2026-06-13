"""
Bluestock Mutual Fund Analytics Capstone

Purpose:
Load mutual fund datasets from the raw data folder,
verify file availability, and perform initial data
quality checks including missing values, duplicates,
data types, and summary statistics.

Author: Unnimaya V Ashok
Date: June 2026
"""

import pandas as pd
import os

data_path = "data/raw"

print("\n=== CHECKING PATH ===")
print("Current folder:", os.getcwd())
print("Data folder exists:", os.path.exists(data_path))

print("\n=== FILES IN DATA/RAW ===")
print(os.listdir(data_path))

csv_files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

print("\nCSV FILES DETECTED:", csv_files)
print("\n===========================\n")

for file in csv_files:
    file_path = os.path.join(data_path, file)

    print(f"\nLOADING: {file}")
    print("--------------------")

    df = pd.read_csv(file_path)

    print("Shape:", df.shape)

    print("\nDtypes:\n", df.dtypes)

    print("\nHead:\n", df.head())

    print("\n--- ANOMALY CHECKS ---")

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nTotal Missing Values:", df.isnull().sum().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\n===========================\n")

import pandas as pd
import os

data_path = "data/raw"

print("\n=== CHECKING PATH ===")
print("Current folder:", os.getcwd())
print("Data folder exists:", os.path.exists(data_path))

print("\n=== FILES IN DATA/RAW ===")
print(os.listdir(data_path))

csv_files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

print("\nCSV FILES DETECTED:", csv_files)
print("\n===========================\n")

for file in csv_files:
    file_path = os.path.join(data_path, file)

    print(f"\nLOADING: {file}")
    print("--------------------")

    df = pd.read_csv(file_path)

    # -----------------------------
    # BASIC INFO
    # -----------------------------
    print("Shape:", df.shape)

    print("\nDtypes:\n", df.dtypes)

    print("\nHead:\n", df.head())

    # -----------------------------
    # ANOMALY CHECKS (ADDED)
    # -----------------------------
    print("\n--- ANOMALY CHECKS ---")

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Total missing values
    print("\nTotal Missing Values:", df.isnull().sum().sum())

    # Duplicates
    print("\nDuplicate Rows:", df.duplicated().sum())

    # Summary stats (numeric only)
    print("\nSummary Statistics:")
    print(df.describe())

    print("\n===========================\n")