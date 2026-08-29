# 💳 Financial Fraud Detection Platform

A real-time financial fraud detection application built with **Python, FastAPI, XGBoost, Streamlit, Pandas, and Postman**. The system provides a REST API for processing transaction requests, validating inputs, generating fraud predictions, and returning actionable transaction decisions.

## 🚀 Features

* RESTful API built with **FastAPI**
* Structured request validation using **Pydantic**
* Real-time fraud prediction using a trained **XGBoost model**
* Transaction feature engineering and model-aligned preprocessing
* Fraud probability and threshold-based **ALLOW/BLOCK** decisions
* Interactive **Streamlit** frontend
* Frontend–backend communication through REST APIs
* API testing using **Postman**
* Error handling for invalid requests and prediction failures

## 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │    Streamlit UI     │
                │  Transaction Input  │
                └──────────┬──────────┘
                           │
                           │ HTTP POST
                           ▼
                ┌─────────────────────┐
                │    FastAPI Server   │
                │                     │
                │ Request Validation  │
                │ Feature Processing  │
                │ Prediction Logic    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   XGBoost Model     │
                │                     │
                │ Fraud Probability   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    API Response     │
                │                     │
                │ Fraud Probability   │
                │ ALLOW / BLOCK       │
                └─────────────────────┘
```

## 🛠️ Technology Stack

| Category         | Technology |
| ---------------- | ---------- |
| Language         | Python     |
| Backend          | FastAPI    |
| API Validation   | Pydantic   |
| Machine Learning | XGBoost    |
| Data Processing  | Pandas     |
| Frontend         | Streamlit  |
| API Testing      | Postman    |
| Model Loading    | Joblib     |

## 📂 Project Structure

```text
financial-fraud-detection/
│
├── app.py
├── Dashboard.py
├── Best Model.pkl
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

### 1. Transaction Request

The user enters transaction information through the Streamlit dashboard, including:

* Transaction type
* Transaction amount
* Originator balances
* Destination balances

The frontend sends the transaction details to the FastAPI `/predict` endpoint as a JSON request.

### 2. Request Validation

FastAPI uses a **Pydantic model** to validate incoming transaction requests and ensure the required fields have the expected data types.

### 3. Feature Processing

The backend performs feature engineering on the transaction and dynamically prepares the input features required by the trained XGBoost model.

### 4. Fraud Prediction

The processed transaction is passed to the XGBoost model, which generates a fraud probability.

A configured threshold is then used to classify the transaction.

```text
Fraud Probability
       │
       ▼
Compare with threshold
       │
   ┌───┴────┐
   │        │
 Fraud    Legitimate
   │        │
 BLOCK     ALLOW
```

### 5. API Response

The API returns a structured JSON response containing the fraud status, probability, and recommended action.

```json
{
  "is_fraud": true,
  "fraud_probability": 0.9234,
  "action": "BLOCK"
}
```

## 🔌 API Endpoints

### Health Check

```http
GET /
```

Returns the current API status and model loading status.

### Fraud Prediction

```http
POST /predict
```

Example request:

```json
{
  "type": "TRANSFER",
  "amount": 10000,
  "oldbalanceOrg": 15000,
  "newbalanceOrig": 5000,
  "oldbalanceDest": 2000,
  "newbalanceDest": 12000
}
```

Example response:

```json
{
  "is_fraud": false,
  "fraud_probability": 0.1245,
  "action": "ALLOW"
}
```

## 🧪 API Testing

The REST API was tested using **Postman** to verify:

* JSON request payloads
* Required transaction fields
* Request validation
* Request limits
* API response structure
* Prediction results
* Error handling

## 💻 Running Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

In another terminal, start the Streamlit dashboard:

```bash
streamlit run Dashboard.py
```

The FastAPI API will be available at:

```text
http://localhost:8000
```

FastAPI also provides interactive API documentation through its built-in documentation interface.

## 🔐 Error Handling

The backend handles situations such as:

* Missing model files
* Invalid transaction requests
* Prediction failures
* API communication errors

Appropriate error responses are returned when backend processing fails.

## 🎯 Project Highlights

* Designed a **RESTful backend architecture** using FastAPI.
* Implemented **structured request validation** using Pydantic.
* Integrated a trained **XGBoost model** into an API-based application.
* Developed **frontend–backend communication** using HTTP requests.
* Tested REST API functionality using **Postman**.
* Implemented **threshold-based transaction decisions** and fraud probability reporting.

## 🔮 Future Improvements

* Add authentication and authorization for API access.
* Add persistent transaction storage using MySQL or MongoDB.
* Implement API rate limiting and monitoring.
* Add automated unit and integration testing.
* Deploy the application to a cloud platform.
* Add centralized logging and application monitoring.

## 👨‍💻 Author

**Brahmajosyula Surya**

B.Tech – Computer Science Engineering
Vishnu Institute of Technology

**GitHub:** https://github.com/surya221718
