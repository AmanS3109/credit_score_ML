import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("wallet_scores.csv")

plt.figure(figsize=(10, 5))
df['score'].hist(bins=20)
plt.title("Wallet Credit Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.tight_layout()
plt.savefig("score_distribution.png")  # Save for GitHub README
plt.show()
