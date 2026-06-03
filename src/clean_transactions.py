import pandas as pd

df = pd.read_csv(
"data/raw/08_investor_transactions.csv"
)

print(df.head())

mapping = {
'sip': 'SIP',
'systematic investment plan': 'SIP',
'lumpsum': 'Lumpsum',
'redemption': 'Redemption'
}

#standardize transaction types
df['transaction_type'] = (
df['transaction_type']
.str.lower()
.map(mapping)
)

#converting transaction dates
df['transaction_date'] = pd.to_datetime(
df['transaction_date'],
errors='coerce'
)

#Check invalid amounts
print("Invalid amounts:")
print(df[df['amount_inr'] <= 0])

print("Invalid amounts:")
print(df[df['amount_inr'] <= 0])

#Keep valid amounts
df = df[df['amount_inr'] > 0]

#Validate KYC status
valid_kyc = [
'Verified',
'Pending',
'Rejected'
]

invalid_kyc = df[
~df['kyc_status'].isin(valid_kyc)
]

print("Invalid KYC rows:")
print(invalid_kyc)

#Save cleaned dataset
df.to_csv(
"data/processed/08_investor_transactions_cleaned.csv",
index=False
)

print("Transaction cleaning completed")