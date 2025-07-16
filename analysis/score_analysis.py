import pandas as pd

df = pd.read_csv("wallet_scores.csv")

# Define buckets
bins = list(range(0, 1100, 100))
labels = [f"{i}-{i+99}" for i in bins[:-1]]
df['score_bucket'] = pd.cut(df['score'], bins=bins, labels=labels, include_lowest=True)

# Count wallets in each bucket
distribution = df['score_bucket'].value_counts().sort_index()
print(distribution)
