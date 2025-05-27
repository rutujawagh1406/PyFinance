import streamlit as st
import pandas as pd
from budget_utils import *

st.set_page_config(page_title="PyFinance Dashboard", layout="wide")

st.title("PyFinance - Personal Budget Tracker")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = load_data("data/sample_data.csv")

st.write("Raw Data", df)

col1, col2, col3 = st.columns(3)
col1.metric("Total Income: ", f"Rs{total_income(df):,.2f}")
col2.metric("Total Expenses: ", f"Rs{total_expense(df):,.2f}")
col3.metric("Net Savings: ", f"Rs{net_savings(df):,.2f}")

st.write("---")
st.write("Expense Breakdown")
fig = plot_expenses(expense_by_category(df))
st.plotly_chart(fig)