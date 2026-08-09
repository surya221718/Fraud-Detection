# Fraud-Detection
💳 Real-Time Financial Fraud Detection & Risk DashboardAn end-to-end machine learning solution designed to detect fraudulent financial transactions in real time. 

Built using the PaySim synthetic transaction dataset, this project combines domain-specific feature engineering, an XGBoost Classifier, and an interactive Streamlit dashboard to deliver instant risk assessment and transaction scoring. 
🚀 Key FeaturesDomain-Specific Feature Engineering: Captures unnatural accounting anomalies through balance discrepancy calculations (errorBalanceOrig and errorBalanceDest). 
High-Risk Transaction Isolation: Filters and targets the specific transaction types prone to fraud (TRANSFER and CASH_OUT). 
Imbalanced Data Handling: Leverages XGBoost optimized for extreme class imbalance to maximize precision and fraud detection recall. 
Interactive Risk Dashboard: Real-time Streamlit web app that accepts live inputs, automatically reconstructs features, and provides immediate risk scores and warning alerts. 
🛠️ Tech StackLanguage: PythonMachine Learning: XGBoost, Scikit-learnData Processing: Pandas, NumPy
Model Persistence: Joblib 
Web Interface: Streamlit  
📊 Data Pipeline & ArchitecturePreprocessing & Domain Filtering:Isolates TRANSFER and CASH_OUT transaction types.  Drops non-predictive identifiers (nameOrig, nameDest, isFlaggedFraud, step).  
Feature Engineering:Origin Balance Error: $\text{errorBalanceOrig} = \text{newbalanceOrig} + \text{amount} - \text{oldbalanceOrg}$  Destination Balance Error: $\text{errorBalanceDest} = \text{oldbalanceDest} + \text{amount} - \text{newbalanceDest}$  Categorical Encoding: Binary mapping for transaction types (type_TRANSFER).  Inference Pipeline:Accepts user transaction details in Streamlit, automatically computes engineered features, and passes standard features into the trained model for instant predictions. 
📈 Model PerformanceMetric
XGBoost Model Score
ROC-AUC Score  0.99
Precision      96%
F1-Score      0.92
