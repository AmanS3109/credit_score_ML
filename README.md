# 🏦 Aave V2 Wallet Credit Scoring

This project builds a transparent credit scoring engine for wallets interacting with the Aave V2 protocol. It processes raw on-chain DeFi transactions, engineers meaningful wallet-level features, and assigns a **score between 0 and 1000** based on behavioral patterns.

> 🔒 Higher scores represent more trustworthy and consistent behavior.  
> ⚠️ Lower scores suggest risk factors such as liquidation, low repayments, or spammy activity.

---

## 📌 Objective

- Parse and preprocess transaction-level data from Aave V2
- Build per-wallet behavior profiles (deposits, borrows, repayments, etc.)
- Compute a rule-based credit score for each wallet
- Analyze scoring behavior with distribution plots and behavior clusters

---

## 📂 Project Structure

scoreModelML/
├── data/
│ └── user-wallet-transactions.json # Raw Aave tx data (JSON)
│
├── src/
│ ├── preprocess.py # Load + clean raw JSON
│ ├── feature_engineering.py # Build wallet-level features
│ ├── score_model.py # Scoring formula
│ └── score_wallets.py # End-to-end script
│
├── analysis/
│ ├── score_analysis.py # Score bucket breakdown & plots
│
├── wallet_features.csv # Features per wallet
├── wallet_scores.csv # Final scores (0–1000)
├── score_distribution.png # Score histogram
├── README.md # 📘 Project overview
└── analysis.md # Score interpretation & analysis

Install dependencies:
```bash
pip install -r requirements.txt

🧑‍💻 Author
Aman Singh
AI/ML Engineer

