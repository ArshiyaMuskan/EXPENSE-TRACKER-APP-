import pandas as pd

def clean_data():
    df = pd.read_csv("data/expenses.csv")

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = pd.to_numeric(df['Amount'])

    df['Category'] = df['Category'].str.strip().str.title()
    df['Type'] = df['Type'].str.strip().str.title()

    df['Month'] = df['Date'].dt.month_name()
    df['Month_Num'] = df['Date'].dt.month
    df['Weekday'] = df['Date'].dt.day_name()

    df.to_csv("data/cleaned_expenses.csv", index=False)

    print("Data cleaned successfully")

if __name__ == "__main__":
    clean_data()
