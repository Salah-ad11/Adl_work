import streamlit as st
import datetime

# --- Logic System ---
salary = 60000
rate_15min = ((salary / 22) / 8) / 4

st.set_page_config(page_title="Al-Adl System", page_icon="⚖️")

st.title("⚖️ Al-Adl Smart System")
st.subheader("Precision in Time.. Justice in Pay")

# --- Interactive Interface ---
user_code = st.text_input("Enter your Security Code", type="password")

col1, col2 = st.columns(2)

with col1:
    if st.button("Check-In"):
        if user_code == "1234":
            st.success(f"Welcome! Logged in at {datetime.datetime.now().strftime('%H:%M:%S')}")
        else:
            st.error("Invalid Code")

with col2:
    if st.button("Check-Out"):
        if user_code == "1234":
            st.info(f"Goodbye! Logged out at {datetime.datetime.now().strftime('%H:%M:%S')}")
            st.write(f"Unit Rate: {round(rate_15min, 2)} DZD")
