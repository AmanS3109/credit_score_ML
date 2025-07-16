# Wallet Credit Score Analysis

This analysis summarizes the results of our wallet credit scoring model, which assigns a score between **0 and 1000** based on historical behavior of users interacting with the Aave V2 protocol.

---

## 📊 Score Distribution

| Score Range | # Wallets |
|-------------|-----------|
| 0–99        | 1         |
| 100–199     | 23        |
| 200–299     | 1773      |
| 300–399     | 527       |
| 400–499     | 269       |
| 500–599     | 357       |
| 600–699     | 318       |
| 700–799     | 191       |
| 800–899     | 38        |
| 900–999     | 0         |

---

### 📉 Histogram: Wallet Score Distribution

![Wallet Credit Score Distribution](score_distribution.png)

This histogram shows the frequency of wallet scores.  
A clear peak is observed between **200–299**, indicating that most wallets had minimal or limited activity on Aave V2.

---

## 🔍 Interpretation of Score Buckets

### 🔴 **Low Score Wallets (0–299)**
- Very limited activity (1–2 transactions)
- No borrowing/repayment behavior
- Likely test wallets, bots, or abandoned accounts

### 🟠 **Mid Score Wallets (300–599)**
- Moderate usage patterns
- Partial repayments or token withdrawals
- Reasonable diversity, low risk

### 🟢 **High Score Wallets (600–899)**
- Strong repayment behavior
- No liquidation events
- Long active periods
- High asset/token diversity

---

## 📌 Insights

- **Over 50%** of wallets scored between **200–299**
- **No wallets** reached the 900–999 range — future models could improve reward weights
- Only **1 wallet** scored below 100 — the model is not overly aggressive

---

## 🔮 Recommendations

- Use these scores as a **credit signal** in lending platforms or DeFi reputation engines
- Improve score weight tuning to differentiate excellent wallets (score > 900)
- Extend to graph-based wallet clustering or time-series modeling

---

## 📈 Conclusion

The current model provides a stable, interpretable signal of user behavior with respect to Aave protocol. While rule-based for now, this scoring system forms a strong foundation for future supervised or hybrid models.
