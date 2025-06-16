File Summarizer — Streamlit Transaction Report Tool

A user-friendly Streamlit web app to upload transaction data CSV files, filter and summarize them by customizable date ranges and timeframes (daily, weekly, monthly, yearly), and generate downloadable CSV reports with success/failure statistics. Designed for quick insights into payment processing data.
Features

    Upload CSV files with transaction data

    Filter data by year and custom date ranges (where applicable)

    Select view modes: daily, weekly, monthly, quarterly, yearly

    Interactive card-based layout for each time segment with previews

    Download CSV summaries and success/failure breakdowns

    View detailed charts on transaction success/failure rates

    Modular backend for easy customization and extension

Installation

    Clone the repository:

git clone git@github.com:greedoftheendless/File-Summarizer.git
cd File-Summarizer

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
.\venv\Scripts\activate    # Windows

Install required packages:

    pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run streamlit_app.py

    Upload your transaction CSV file.

    Select the desired year and date range.

    Choose the view type (daily, weekly, monthly, quarterly, yearly).

    Click through the summary cards to preview data and download reports.

    View charts for detailed success/failure analytics.

Data Format Requirements

Your CSV file should include at least these columns:

    Transaction Date

    Payment Method

    Transaction Status

    Transaction Type

Ensure Transaction Status includes statuses such as Completed, Failed, Pending (Pending transactions are excluded from success/failure calculations).
Project Structure

    streamlit_app.py: Main Streamlit user interface

    shared/: Helper modules for data processing and report generation

    requirements.txt: Python dependencies

Contributing

Contributions are welcome! Please open issues or submit pull requests for bugs, features, or improvements.
License

This project is licensed under the MIT License.
