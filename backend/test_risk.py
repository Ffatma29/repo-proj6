from services.risk_service import calculate_risk

test_scores = [
   0.10,
   -0.05,
   -0.20,
   -0.40,
   -0.70,
]

for score in test_scores:
   risk = calculate_risk(score)
   print(f"Score: {score} -> Risk: {risk}")