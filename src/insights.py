import pandas as pd

def generate_insights():
    df = pd.read_csv("data/cleaned_expenses.csv")

    category_total = df.groupby('Category')['Amount'].sum()

    top_category = category_total.idxmax()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    total_income = df[df['Type'] == 'Income']['Amount'].sum()

    print("\nINSIGHTS")
    print("Top Category:", top_category)
    print("Total Expense:", total_expense)
    print("Total Income:", total_income)

    if total_expense > total_income:
        print("Overspending detected")
    else:
        print("You are saving money")

if __name__ == "__main__":
    generate_insights()