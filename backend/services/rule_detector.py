import pandas as pd

def rule_based_detection(df: pd.DataFrame) -> pd.Series:
   suspicious = df["num_failed_logins"] >= 5
   return suspicious.astype(int)