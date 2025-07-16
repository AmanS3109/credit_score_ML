import pandas as pd

def normalize(x, min_val, max_val):
    """Clamp x into [min_val, max_val] and rescale to [0,1]."""
    if x <= min_val:
        return 0.0
    if x >= max_val:
        return 1.0
    return (x - min_val) / (max_val - min_val)

def compute_score(row):
    # --- 1) Normalized sub‑scores with tighter thresholds ---
    # Repay ratio: only 80%–100% gets credit
    repay = normalize(row['repay_ratio'], 0.8, 1.0)

    # Zero liquidations = full; any liquidation = zero
    no_liq = 1.0 if row['n_liquidation'] == 0 else 0.0

    # Active days: minimum 30 days, saturates at 365 days
    days = normalize(row['active_days'], 30, 365)

    # Token diversity: 3–10 unique assets
    diversity = normalize(row['n_assets'], 3, 10)

    # Borrow/Deposit ratio: 0–1 healthy leverage
    borrow_ratio = normalize(
        (row['total_borrow_usd'] / row['total_deposit_usd'])
        if row['total_deposit_usd'] > 0 else 0.0,
        0.0, 1.0
    )

    # Redeem ratio: full range [0–1]
    redeem = normalize(row['redeem_ratio'], 0.0, 1.0)

    # Transaction frequency penalty: 0.1–5 tx/day, invert so lower freq is better
    freq = 1.0 - normalize(row['tx_per_day'], 0.1, 5.0)

    # --- 2) Weighted sum (total = 1,050 before cap) ---
    raw = (
        250 * repay +
        250 * no_liq +
        200 * borrow_ratio +
        150 * days +
        100 * diversity +
         50 * redeem +
         50 * freq
    )

    # Cap at 1000 and round
    score = min(1000, int(raw))

    # --- 3) Elite bonus for truly stellar wallets ---
    # Must repay ≥99%, zero liquidations, and full-year active
    if repay >= 0.99 and no_liq == 1.0 and days >= 1.0:
        score = min(1000, score + 25)

    return score
