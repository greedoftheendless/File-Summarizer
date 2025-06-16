import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_success_failure_pie_chart(summary_path, timeframe_label):
    df = pd.read_csv(summary_path)

    if 'Success %' not in df.columns or 'Failure %' not in df.columns:
        st.warning(f"Missing 'Success %' or 'Failure %' in {timeframe_label} summary file.")
        return

    for _, row in df.iterrows():
        method = row['Payment Method']
        sizes = [row['Success %'], row['Failure %']]
        labels = ['Success', 'Failure']
        colors = ['#4CAF50', '#F44336']  # Green and Red

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90
        )
        ax.axis('equal')
        plt.title(f"{method} - {timeframe_label} View")
        st.pyplot(fig)
