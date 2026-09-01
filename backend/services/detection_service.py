from services.prediction_service import predict_threat
from services.rule_detector import rule_based_detection
import pandas as pd


def detect_threat(data: dict) -> dict:
    df = pd.DataFrame([data])

    rule_result = int(rule_based_detection(df).iloc[0])

    ml_result = predict_threat(data)

    return {
        "classification": (
            "Suspicious Activity"
            if ml_result["status"] == "Attack"
            else "Normal Activity"
        ),
        "status": ml_result["status"],
        "anomaly_score": ml_result["anomaly_score"],
        "risk_level": ml_result["risk_level"],
        "rule_based_detection": bool(rule_result),
    }
