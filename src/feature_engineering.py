import pandas as pd
import numpy as np
from tqdm import tqdm

def extract_usd(row):
    try:
        token = row['actionData'].get('assetSymbol', '').upper()
        amount = float(row['actionData'].get('amount', 0))
        price = float(row['actionData'].get('assetPriceUSD', 0))

        # Set decimals by token type
        if token in ['USDC', 'USDT', 'DAI']:
            decimals = 1e6  # 6 decimals
        else:
            decimals = 1e18  # assume 18 decimals for ETH, WETH, etc.

        return (amount / decimals) * price
    except:
        return 0


def build_wallet_features(df):
    df['usd_value'] = df.apply(extract_usd, axis=1)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    grouped = df.groupby('userWallet')

    features = []

    for wallet, group in tqdm(grouped):
        actions = group['action'].value_counts().to_dict()

        deposit_usd = group[group['action'] == 'deposit']['usd_value'].sum()
        borrow_usd = group[group['action'] == 'borrow']['usd_value'].sum()
        repay_usd = group[group['action'] == 'repay']['usd_value'].sum()
        redeem_usd = group[group['action'] == 'redeemunderlying']['usd_value'].sum()

        first_seen = group['timestamp'].min()
        last_seen = group['timestamp'].max()
        active_days = max(1, (last_seen - first_seen).days)

        features.append({
            'wallet': wallet,
            'n_tx': len(group),
            'n_deposit': actions.get('deposit', 0),
            'n_borrow': actions.get('borrow', 0),
            'n_repay': actions.get('repay', 0),
            'n_redeem': actions.get('redeemunderlying', 0),
            'n_liquidation': actions.get('liquidationcall', 0),
            'total_deposit_usd': deposit_usd,
            'total_borrow_usd': borrow_usd,
            'total_repay_usd': repay_usd,
            'total_redeem_usd': redeem_usd,
            'repay_ratio': repay_usd / borrow_usd if borrow_usd > 0 else 0,
            'redeem_ratio': redeem_usd / deposit_usd if deposit_usd > 0 else 0,
            'active_days': active_days,
            'tx_per_day': len(group) / active_days,
            'n_assets': group['actionData'].apply(lambda x: x.get('assetSymbol')).nunique()
        })

    return pd.DataFrame(features)
