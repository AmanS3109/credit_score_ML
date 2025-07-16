import pandas as pd

def normalize(x, min_val, max_val):
    return min(1, max(0, (x - min_val) / (max_val - min_val))) if max_val != min_val else 0

def compute_score(row):
    repay_ratio = normalize(row['repay_ratio'], 0, 1)
    redeem_ratio = normalize(row['redeem_ratio'], 0, 1)
    n_liquidation = row['n_liquidation']
    active_days = normalize(row['active_days'], 0, 90)
    tx_per_day = normalize(row['tx_per_day'], 0.1, 5)
    borrow_ratio = normalize(
        row['total_borrow_usd'] / row['total_deposit_usd'] if row['total_deposit_usd'] > 0 else 0,
        0, 1.5
    )
    diversity = normalize(row['n_assets'], 1, 5)

    score = (
        200 * repay_ratio +
        100 * redeem_ratio +
        200 * (1 if n_liquidation == 0 else 0.2) +
        100 * active_days +
        100 * (1 - tx_per_day) +
        200 * borrow_ratio +
        100 * diversity
    )
    return int(min(1000, score))
