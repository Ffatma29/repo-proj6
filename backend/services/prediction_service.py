import joblib
import pandas as pd
from services.feature_engineering import prepare_features
from services.risk_service import calculate_risk

MODEL_PATH = "models/isolation_forest.joblib"

saved_model = joblib.load(MODEL_PATH)
model = saved_model["model"]
feature_columns = saved_model["feature_columns"]

def predict_threat(data: dict) -> dict:
   df = pd.DataFrame([data])
   features = prepare_features(df)
   features = features.reindex(
       columns=feature_columns,
       fill_value=0
   )
   prediction = model.predict(features)[0]
   anomaly_score = model.decision_function(features)[0]
   status = "Attack" if prediction == -1 else "Normal"
   risk_level = calculate_risk(anomaly_score)
   return {
       "status": status,
       "anomaly_score": round(float(anomaly_score), 4),
       "risk_level": risk_level
   }