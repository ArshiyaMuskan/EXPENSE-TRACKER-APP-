
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💰 Expense Tracker Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/cleaned_expenses.csv")
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        return df
    except:
        return pd.DataFrame()

df = load_data()

# -----------------------------
# CHECK DATA
# -----------------------------
if df.empty:
    st.error("❌ No data found. Run main.py first.")
    st.stop()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Select Category",
    df['Category'].unique(),
    default=df['Category'].unique()
)

transaction_type = st.sidebar.selectbox(
    "Select Type",
    ["All", "Expense", "Income"]
)

# Apply filters
filtered_df = df[df['Category'].isin(category)]

if transaction_type != "All":
    filtered_df = filtered_df[filtered_df['Type'] == transaction_type]

# -----------------------------
# HANDLE EMPTY FILTER
# -----------------------------
if filtered_df.empty:
    st.warning("⚠️ No data for selected filters")
    st.stop()

# -----------------------------
# METRICS
# -----------------------------
total_expense = filtered_df[filtered_df['Type'] == 'Expense']['Amount'].sum()
total_income = filtered_df[filtered_df['Type'] == 'Income']['Amount'].sum()
balance = total_income - total_expense

col1, col2, col3 = st.columns(3)

col1.metric("💸 Expense", f"₹{total_expense}")
col2.metric("💰 Income", f"₹{total_income}")
col3.metric("📊 Balance", f"₹{balance}")

# -----------------------------
# CATEGORY CHART
# -----------------------------
st.subheader("📊 Category-wise Spending")

category_data = filtered_df.groupby('Category')['Amount'].sum()

if not category_data.empty:
    plt.figure()
    category_data.plot(kind='bar')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("No category data available")

# -----------------------------
# PIE CHART
# -----------------------------
st.subheader("🍕 Expense Distribution")

expense_df = filtered_df[filtered_df['Type'] == 'Expense']
expense_data = expense_df.groupby('Category')['Amount'].sum()

if not expense_data.empty:
    plt.figure()
    expense_data.plot(kind='pie', autopct='%1.1f%%')
    st.pyplot(plt)
else:
    st.write("No expense data available")

# -----------------------------
# MONTHLY TREND
# -----------------------------
st.subheader("📈 Monthly Trend")

monthly = filtered_df.groupby('Month')['Amount'].sum()

if not monthly.empty:
    plt.figure()
    monthly.plot(marker='o')
    st.pyplot(plt)
else:
    st.write("No monthly data available")

# -----------------------------
# RAW DATA
# -----------------------------
if st.checkbox("Show Data"):
    st.dataframe(filtered_df)

# -----------------------------
# INSIGHTS
# -----------------------------
st.subheader("🔍 Insights")

if total_expense > total_income:
    st.error("⚠️ You are overspending!")
else:
    st.success("✅ You are saving money!")

if not category_data.empty:
    top_category = category_data.idxmax()
    st.info(f"🏆 Top Category: {top_category}")


