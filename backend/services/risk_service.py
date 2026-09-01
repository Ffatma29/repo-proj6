def calculate_risk(anomaly_score: float) -> str:
   if anomaly_score >= 0:
       return "Normal"
   elif anomaly_score >= -0.1:
       return "Low"
   elif anomaly_score >= -0.3:
       return "Medium"
   elif anomaly_score >= -0.5:
       return "High"
   else:
       return "Critical"
