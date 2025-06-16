import streamlit as st
import os
import pandas as pd
from datetime import datetime
from shared.sorter import sort_transactions
from shared.summarizer import generate_summary
from shared.chart import plot_success_failure_pie_chart

st.set_page_config(page_title="Transaction Summary Generator", layout="wide")
st.title("📊 Transaction Summary Generator")

uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

    if 'Transaction Date' not in df.columns:
        st.error("Uploaded file must contain a 'Transaction Date' column.")
    else:
        df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
        year_selected = st.selectbox("Select year", sorted(df['Transaction Date'].dt.year.unique(), reverse=True))

        timeframes = ['Daily', 'Weekly', 'Monthly', 'Yearly']
        timeframe = st.radio("Select timeframe to view and analyze", timeframes)

        start_date = None
        end_date = None
        label = timeframe.lower()

        if timeframe in ['Daily', 'Weekly']:
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input(f"Start Date for {timeframe}", value=df['Transaction Date'].min().date())
            with col2:
                end_date = st.date_input(f"End Date for {timeframe}", value=df['Transaction Date'].max().date())

        sorted_csv = sort_transactions(df, label, year_selected, start_date, end_date)

        if sorted_csv:
            st.success(f"✅ Sorted transactions saved for {label.title()}.")

            preview_df = pd.read_csv(sorted_csv)
            st.dataframe(preview_df.head())

            with open(sorted_csv, "rb") as f:
                st.download_button(
                    label=f"Download Sorted {timeframe} CSV",
                    data=f,
                    file_name=os.path.basename(sorted_csv),
                    mime="text/csv"
                )

            summary_path = generate_summary(sorted_csv, label)

            if summary_path is None:
                st.warning(f"No completed or failed transactions found after removing 'Pending' from {label} data.")
            else:
                with open(summary_path, "rb") as f:
                    st.download_button(
                        label=f"Download Summary CSV for {timeframe}",
                        data=f,
                        file_name=os.path.basename(summary_path),
                        mime="text/csv"
                    )

                st.subheader(f"Success vs Failure Pie Chart - {timeframe} View")
                plot_success_failure_pie_chart(summary_path, timeframe)

        else:
            st.warning(f"No {timeframe} data available for the selected filters.")
