import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("💱 Currency Converter")
st.markdown("Convert from one currency to another using live exchange rates.")

# Input fields
amount = st.number_input("Amount", min_value=0.0, value=100.0)
source_currency = st.text_input("From Currency (e.g. USD)", value="USD")
target_currency = st.text_input("To Currency (e.g. INR)", value="INR")

# Convert button
if st.button("Convert"):
    try:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={source_currency}&to={target_currency}"
        response = requests.get(url).json()

        if "rates" in response and target_currency in response["rates"]:
            converted = response["rates"][target_currency]
            st.success(f"{amount} {source_currency} is {converted} {target_currency}")
        else:
            st.error("Conversion failed. Please check currency codes.")
    except Exception as e:
        st.error(f"Error: {e}")