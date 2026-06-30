import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Title and Intro
st.title("💰 Personal Budget Tracker")
st.subheader("Let's map out your monthly finances!")

# 2. Income Section
st.header("💵 Income")
income = st.number_input("Total Monthly Income ($):", min_value=0.0, value=2500.0, step=50.0)

# 3. Expenses Section
st.header("📉 Expenses")
st.write("Enter your spending for each category below:")

groceries = st.number_input("Groceries ($):", min_value=0.0, value=300.0, step=10.0)
gas = st.number_input("Gas/Transportation ($):", min_value=0.0, value=150.0, step=10.0)
entertainment = st.number_input("Entertainment ($):", min_value=0.0, value=100.0, step=10.0)
other = st.number_input("Other Expenses ($):", min_value=0.0, value=200.0, step=10.0)

# 4. Math and Calculations
total_expenses = groceries + gas + entertainment + other
savings = income - total_expenses

# 5. Display Summary Metrics
st.divider()
st.subheader("📊 Your Summary")

col1, col2 = st.columns(2)
col1.metric(label="Total Expenses", value=f"${total_expenses:,.2f}")
col2.metric(label="Remaining Savings", value=f"${savings:,.2f}")

# 6. Feedback Messages
if savings > 0:
    st.success("Great job! You are saving money this month. 🎉")
elif savings == 0:
    st.info("You are breaking exactly even.")
else:
    st.error("Warning: Your expenses exceed your income! ⚠️")

# 7. The Pie Chart
st.subheader("🍕 Expense Breakdown")

chart_data = pd.DataFrame({
    "Category": ["Groceries", "Gas", "Entertainment", "Other"],
    "Amount": [groceries, gas, entertainment, other]
})

if total_expenses > 0:
    fig = px.pie(chart_data, values="Amount", names="Category", hole=0.4)
    st.plotly_chart(fig)
else:
    st.info("Enter some expenses above to see your chart breakdown!")
