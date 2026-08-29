import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Fraud Detection API")


class TransactionInput(BaseModel):
    type: str
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float


MODEL_PATH = "Best Model.pkl"
OPTIMAL_THRESHOLD = 0.50

# Load Model
model = "Best Model.pkl"
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        print("✅ Model successfully loaded!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
else:
    print(
        f"❌ Model file NOT found at '{MODEL_PATH}'. Place 'Saved Model.pkl' in this folder."
    )


@app.get("/")
def health_check():
    return {"status": "online", "model_loaded": model is not None}


@app.post("/predict")
def predict(transaction: TransactionInput):
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model file is not loaded. Check server terminal logs.",
        )

    try:
        # Convert incoming JSON payload to DataFrame
        data = pd.DataFrame([transaction.model_dump()])

        # 1. Feature Engineering
        data["errorBalanceOrig"] = (
            data["newbalanceOrig"] + data["amount"] - data["oldbalanceOrg"]
        )
        data["errorBalanceDest"] = (
            data["oldbalanceDest"] + data["amount"] - data["newbalanceDest"]
        )

        # 2. Extract expected feature names directly from the trained XGBoost model
        expected_features = model.get_booster().feature_names

        # 3. Dynamic One-Hot Encoding based on trained model requirements
        for feat in expected_features:
            if feat not in data.columns:
                if feat.startswith("type_"):
                    type_val = feat.replace("type_", "")
                    data[feat] = (data["type"] == type_val).astype(int)
                else:
                    data[feat] = 0

        # Drop original unencoded 'type' column
        if "type" in data.columns:
            data = data.drop(columns=["type"])

        # Reorder columns to match model expectations
        data_processed = data[expected_features]

        # Predict probability
        prob = float(model.predict_proba(data_processed)[0][1])
        is_fraud = bool(prob >= OPTIMAL_THRESHOLD)

        return {
            "is_fraud": is_fraud,
            "fraud_probability": round(prob, 4),
            "action": "BLOCK" if is_fraud else "ALLOW",
        }

    except Exception as e:
        # Print actual error message to terminal logs
        print(f"\n❌ PREDICTION ERROR: {e}\n")
        raise HTTPException(
            status_code=500, detail=f"Prediction Error: {str(e)}"
        )