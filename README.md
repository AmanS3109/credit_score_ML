# 🏦 Wallet Credit Scoring

This project implements a credit scoring system for wallets interacting with the Aave V2 protocol. It analyzes raw transaction-level data, extracts behavioral features, and assigns an interpretable score from 0 to 1000 to each wallet.

- 🟢 **Higher scores** = trustworthy, consistent DeFi users  
- 🔴 **Lower scores** = risky, bot-like, or poorly behaving users  

---

## 🧠 Objective

1. Parse raw on-chain Aave V2 data  
2. Engineer meaningful wallet features  
3. Score wallets based on behavioral rules  
4. Analyze distribution and interpret behavior by score range  

---

## 📂 Project Structure

    scoreModelML/
    ├── data/
    │   └── user-wallet-transactions.json        # Raw Aave tx data (JSON)
    ├── src/
    │   ├── preprocess.py                        # Load + clean raw JSON
    │   ├── feature_engineering.py               # Build wallet-level features
    │   ├── score_model.py                       # Scoring formula
    │   └── score_wallets.py                     # End-to-end pipeline script
    ├── analysis/
    │   └── score_analysis.py                    # Score bucket breakdown & plots
    ├── wallet_features.csv                      # Features per wallet (intermediate)
    ├── wallet_scores.csv                        # Final scores (0–1000)
    ├── score_distribution.png                   # Score histogram
    ├── README.md                                # 📘️ Project overview
    └── analysis.md                              # 📊 Score interpretation & insights

---

## ⚙️ How to Run

1. **Install requirements**  
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the pipeline**  
   ```bash
   python src/score_wallets.py
   ```
   This will:  
   - Load the raw data  
   - Engineer wallet features  
   - Score each wallet  
   - Save `wallet_scores.csv`  

3. **Generate analysis**  
   ```bash
   python analysis/score_analysis.py
   ```  
   Outputs:  
   - Score distribution counts  
   - `score_distribution.png` (graph)  
   - Summary for `analysis.md`

---

## 🧶 Scoring Logic

| Feature Component       | Weight |
|-------------------------|--------|
| Repay ratio             | 200    |
| Redeem ratio            | 100    |
| No liquidation history  | 200    |
| Active days             | 100    |
| Transaction frequency   | 100    |
| Borrow/Deposit ratio    | 200    |
| Token diversity         | 100    |

- Scores are normalized, weighted, and then capped at a maximum of **1000**.

---

## 📊 Example Score Distribution

![Score Distribution](analysis/score_distribution.png)

---

## 📝 Sample Scores

| Wallet Address      | Score |
|---------------------|-------|
| `0x0000...d4b6`     | 282   |
| `0x0000...3852c`    | 504   |
| `0x0000...7bf1ee`   | 708   |

> ➡️ See: `wallet_scores.csv`

---

## ✅ Included

- Clean modular code in `src/`  
- Fully interpretable scoring logic  
- Ready-to-run scripts  
- Data visualization  
- Professional documentation  

---

## 👨‍💼 Author

**Aman Singh**  
AI/ML Engineer  
