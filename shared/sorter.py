import pandas as pd
import os

def sort_transactions(df, label, year_selected, start_date=None, end_date=None):
    df = df.copy()
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    df = df[df['Transaction Date'].dt.year == year_selected]

    if label in ['daily', 'weekly'] and start_date and end_date:
        df = df[(df['Transaction Date'].dt.date >= start_date) & (df['Transaction Date'].dt.date <= end_date)]

    if df.empty:
        return None

    if label == 'daily':
        df['Period'] = df['Transaction Date'].dt.date
    elif label == 'weekly':
        df['Period'] = df['Transaction Date'].dt.to_period('W').apply(lambda r: r.start_time.date())
    elif label == 'monthly':
        df['Period'] = df['Transaction Date'].dt.to_period('M').astype(str)
    elif label == 'yearly':
        df['Period'] = df['Transaction Date'].dt.year

    output_path = f"sorted_{label}.csv"
    df.to_csv(output_path, index=False)
    return output_path
