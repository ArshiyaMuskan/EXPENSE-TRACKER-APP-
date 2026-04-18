import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visuals():
    os.makedirs("outputs", exist_ok=True)

    df = pd.read_csv("data/cleaned_expenses.csv")

    category_total = df.groupby('Category')['Amount'].sum()

    # Bar Chart
    plt.figure(figsize=(10,5))
    sns.barplot(x=category_total.index, y=category_total.values)
    plt.xticks(rotation=45)
    plt.title("Category-wise Spending")
    plt.savefig("outputs/category.png")
    plt.close()

    # Pie Chart
    expense_df = df[df['Type'] == 'Expense']
    expense_category = expense_df.groupby('Category')['Amount'].sum()

    plt.figure(figsize=(7,7))
    plt.pie(expense_category, labels=expense_category.index, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.savefig("outputs/pie.png")
    plt.close()

    print("Charts saved successfully")

if __name__ == "__main__":
    create_visuals()