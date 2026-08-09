import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="PaySim Fraud Detection Platform", layout="centered")

st.title("🛡️ PaySim Wire Transfer Fraud Detection Hub")
st.markdown("Evaluate financial transactions in real-time using your trained XGBoost model.")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("Transaction Amount", min_value=0.0, value=250000.0)
    oldbalanceOrg = st.number_input("Sender's Old Balance", min_value=0.0, value=250000.0)
    newbalanceOrig = st.number_input("Sender's New Balance", min_value=0.0, value=0.0)
with col2:
    oldbalanceDest = st.number_input("Receiver's Old Balance", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("Receiver's New Balance", min_value=0.0, value=250000.0)
    tx_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT"])

st.markdown("---")

if st.button("Analyze Transaction", type="primary", use_container_width=True):
    try:
        model = joblib.load('Saved Model.pkl')
        
        # Recreate the exact feature engineering used during model training
        input_data = pd.DataFrame([{
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceOrig': newbalanceOrig,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest,
            'errorBalanceOrig': newbalanceOrig + amount - oldbalanceOrg,
            'errorBalanceDest': oldbalanceDest + amount - newbalanceDest,
            'type_TRANSFER': 1 if tx_type == 'TRANSFER' else 0
        }])
        
        prob = model.predict_proba(input_data)[0, 1]
        
        st.markdown("### 📊 Evaluation Results")
        if prob >= 0.5:
            st.error(f"🚨 **FRAUD DETECTED!** Risk Probability: **{prob * 100:.2f}%**")
            st.warning("⚠️ This transaction exhibits balance discrepancies typical of fraudulent fund draining.")
        else:
            st.success(f"✅ **LEGITIMATE TRANSACTION.** Risk Probability: **{prob * 100:.2f}%**")
            st.info("ℹ️ Transaction matches normal operational balance constraints.")
            
    except FileNotFoundError:
        st.error("⚠️ Model file `fraud_detector_model.pkl` not found. Please place it in the same directory as `app.py`.")