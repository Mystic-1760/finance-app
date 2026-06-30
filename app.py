import streamlit as st

# Set up the title of your web page
st.title("💰 Personal Budget Tracker")
st.subheader("Let's map out your monthly finances!")

# Income section
st.header("💵 Income")
income = st.number_input("Total Monthly Income ($):", min_value=0.0, value=2500.0, step=50.0)

# Expenses section
st.header("📉 Expenses")
st.write("Enter your spending for each category below:")

groceries = st.number_input("Groceries ($):", min_value=0.0, value=300.0, step=10.0)
gas = st.number_input("Gas/Transportation ($):", min_value=0.0, value=150.0, step=10.0)
entertainment = st.number_input("Entertainment ($):", min_value=0.0, value=100.0, step=10.0)
other = st.number_input("Other Expenses ($):", min_value=0.0, value=200.0, step=10.0)

# Calculations
total_expenses = groceries + gas + entertainment + other
savings = income - total_expenses

# Display results
st.divider()
st.subheader("📊 Your Summary")

# Show total expenses and remaining savings side-by-side using columns
col1, col2 = st.columns(2)
col1.metric(label="Total Expenses", value=f"${total_expenses:,.2f}")
col2.metric(label="Remaining Savings", value=f"${savings:,.2f}")

# Give the user feedback based on their savings
if savings > 0:
    st.success("Great job! You are saving money this month. 🎉")
elif savings == 0:
    st.info("You are breaking exactly even.")
else:
    st.error("Warning: Your expenses exceed your income! ⚠️")
