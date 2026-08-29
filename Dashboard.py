import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Fraud Detection Dashboard", layout="centered")

st.title("💳 Real-Time Transaction Fraud Detector")
st.write("Input transaction parameters below to evaluate fraud risk.")

# API Endpoint URL (Local FastAPI)
API_URL = "http://127.0.0.1:8000/predict"

# Input Form
with st.form("transaction_form"):
    transaction_type = st.selectbox(
        "Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT", "CASH_IN"]
    )
    amount = st.number_input(
        "Amount ($)", min_value=0.0, value=10000.0, step=100.0
    )

    col1, col2 = st.columns(2)
    with col1:
        oldbalanceOrg = st.number_input(
            "Originator Initial Balance ($)", min_value=0.0, value=10000.0
        )
        newbalanceOrig = st.number_input(
            "Originator New Balance ($)", min_value=0.0, value=0.0
        )
    with col2:
        oldbalanceDest = st.number_input(
            "Destination Initial Balance ($)", min_value=0.0, value=0.0
        )
        newbalanceDest = st.number_input(
            "Destination New Balance ($)", min_value=0.0, value=10000.0
        )

    submit_btn = st.form_submit_button("Analyze Risk")

if submit_btn:
    payload = {
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            prob = result["fraud_probability"] * 100

            st.divider()
            st.subheader("Assessment Result")

            if result["is_fraud"]:
                st.error(f"🚨 **{result['action']}: High Fraud Risk Detected**")
            else:
                st.success(f"✅ **{result['action']}: Transaction Legitimate**")

            st.progress(int(prob))
            st.metric(label="Fraud Probability Score", value=f"{prob:.2f}%")
        else:
            st.error("API returned an error. Make sure FastAPI server is running.")
    except Exception as e:
        st.error(f"Could not connect to FastAPI server at {API_URL}. Start `uvicorn app:app` first.")