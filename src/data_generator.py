import pandas as pd
import numpy as np
import os

def generate_data():
    os.makedirs("data", exist_ok=True)

    np.random.seed(42)

    dates = pd.date_range(start="2024-01-01", periods=365)

    categories = ['Food', 'Travel', 'Rent', 'Shopping', 'Bills']
    payment_methods = ['Cash', 'Card', 'UPI']
    types = ['Expense', 'Income']

    data = {
        "Date": np.random.choice(dates, 150),
        "Category": np.random.choice(categories, 150),
        "Amount": np.random.randint(100, 5000, 150),
        "Payment_Method": np.random.choice(payment_methods, 150),
        "Type": np.random.choice(types, 150, p=[0.8, 0.2])
    }

    df = pd.DataFrame(data)
    df.to_csv("data/expenses.csv", index=False)

    print("Data generated successfully")

if __name__ == "__main__":
    generate_data()
