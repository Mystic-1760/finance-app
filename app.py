import streamlit as st

# Set up the title of your web page
st.title("💰 Personal Budget Tracker")
st.subheader("Welcome! Let's map out your monthly finances.")

# User inputs
income = st.number_input("Enter your monthly income ($):", min_value=0.0, value=2000.0, step=50.0)
expenses = st.number_input("Enter your monthly expenses ($):", min_value=0.0, value=1200.0, step=50.0)

# Calculations
savings = income - expenses

# Display results
st.divider()
st.metric(label="Remaining Monthly Savings", value=f"${savings:,.2f}")

if savings > 0:
    st.success("Great job! You are saving money this month. 🎉")
elif savings == 0:
    st.info("You are breaking exactly even.")
else:
    st.error("Warning: Your expenses exceed your income! ⚠️")
