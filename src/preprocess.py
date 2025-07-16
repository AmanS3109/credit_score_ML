# 1st task -->  clean and tranform json

import json
import pandas as pd

with open(r'data/user-wallet-transactions.json') as f:
    raw_data = json.load(f)

# assuming data is a list of dicts per transaction

df = pd.DataFrame(raw_data)
# print(df.head())
# print(df.columns)

# print(df['action'].value_counts())

# print(df['actionData'].iloc[0])   # First record

# print(df['actionData'].apply(lambda x: list(x.keys()) if isinstance(x, dict) else None).value_counts())

# print(df.columns)
# if 'wallet' in df.columns:
    # print(df['wallet'].head())
# elif 'actionData' in df.columns:
    # print(df['actionData'].iloc[0])  # might contain 'user' or 'wallet'

from feature_engineering import build_wallet_features

features_df = build_wallet_features(df)
# print(features_df.head())
features_df.to_csv("wallet_features.csv", index=False)
print(features_df.shape)

