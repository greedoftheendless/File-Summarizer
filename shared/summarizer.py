import pandas as pd

def generate_summary(sorted_csv_path, label):
    df = pd.read_csv(sorted_csv_path)

    df = df[df['Transaction Status'].isin(['Completed', 'Failed'])]

    if df.empty:
        return None

    summary = []

    for method in df['Payment Method'].unique():
        method_df = df[df['Payment Method'] == method]
        total = len(method_df)
        success = len(method_df[method_df['Transaction Status'] == 'Completed'])
        failure = len(method_df[method_df['Transaction Status'] == 'Failed'])
        summary.append({
            'Payment Method': method,
            'Total': total,
            'Success Count': success,
            'Failure Count': failure,
            'Success %': round((success / total) * 100, 2),
            'Failure %': round((failure / total) * 100, 2),
        })

    summary_df = pd.DataFrame(summary)
    output_path = f"summary_{label}.csv"
    summary_df.to_csv(output_path, index=False)
    return output_path
