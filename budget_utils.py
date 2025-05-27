import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def load_data(csv_path):
    return pd.read_csv(csv_path)

def total_income(df):
    return df[df['Type'] == 'Income']['Amount'].sum()

def total_expense(df):
    return df[df['Type'] == 'Expense']['Amount'].sum()

def net_savings(df):
    return total_income(df) - total_expense(df)

def expense_by_category(df):
    return df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

def plot_expenses(expense_data):
    fig = px.pie(values=expense_data.values, names=expense_data.index, title='Expense by category')
    return fig