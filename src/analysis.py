import pandas as pd

def analyze_data():
    df = pd.read_csv("data/cleaned_expenses.csv")

    category_total = df.groupby('Category')['Amount'].sum()
    monthly_expense = df[df['Type'] == 'Expense'].groupby('Month_Num')['Amount'].sum()
    monthly_income = df[df['Type'] == 'Income'].groupby('Month_Num')['Amount'].sum()

    print("\nCategory-wise Spending:\n", category_total)
    print("\nMonthly Expense:\n", monthly_expense)

    return category_total, monthly_expense, monthly_income

if __name__ == "__main__":
    analyze_data()
    