from feature_engineering import build_wallet_features
from score_model import compute_score
import pandas as pd
import json

with open("data/user-wallet-transactions.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
features_df = build_wallet_features(df)
features_df['score'] = features_df.apply(compute_score, axis=1)
features_df[['wallet', 'score']].to_csv("wallet_scores.csv", index=False)
print(features_df.head())