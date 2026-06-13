"""
Master execution script for Bluestock Mutual Fund Analytics Capstone
"""

import subprocess

print("=" * 50)
print("Bluestock Mutual Fund Analytics Pipeline")
print("=" * 50)

subprocess.run(["python", "data_ingestion.py"])
subprocess.run(["python", "fetch_nav.py"])
subprocess.run(["python", "fund_master_analysis.py"])

print("\nPipeline completed successfully.")