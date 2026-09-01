import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from services.feature_engineering import prepare_features

DATA_PATH = "data/kddcup.data_10_percent.txt"
COLUMNS = [
   "duration",
   "protocol_type",
   "service",
   "flag",
   "src_bytes",
   "dst_bytes",
   "land",
   "wrong_fragment",
   "urgent",
   "hot",
   "num_failed_logins",
   "logged_in",
   "num_compromised",
   "root_shell",
   "su_attempted",
   "num_root",
   "num_file_creations",
   "num_shells",
   "num_access_files",
   "num_outbound_cmds",
   "is_host_login",
   "is_guest_login",
   "count",
   "srv_count",
   "serror_rate",
   "srv_serror_rate",
   "rerror_rate",
   "srv_rerror_rate",
   "same_srv_rate",
   "diff_srv_rate",
   "srv_diff_host_rate",
   "dst_host_count",
   "dst_host_srv_count",
   "dst_host_same_srv_rate",
   "dst_host_diff_srv_rate",
   "dst_host_same_src_port_rate",
   "dst_host_srv_diff_host_rate",
   "dst_host_serror_rate",
   "dst_host_srv_serror_rate",
   "dst_host_rerror_rate",
   "dst_host_srv_rerror_rate",
   "label",
]

df = pd.read_csv(
   DATA_PATH,
   header=None,
   names=COLUMNS,
   on_bad_lines="skip",
)
print("Dataset loaded:", df.shape)
X = prepare_features(df)
print("Features:", X.shape)

# Train only on normal behavior
normal_mask = df["label"] == "normal."
X_normal = X[normal_mask]
print("Normal training samples:", X_normal.shape)

model = IsolationForest(
   n_estimators=100,
   contamination=0.05,
   random_state=42,
   n_jobs=-1,
)
model.fit(X_normal)
print("Isolation Forest trained successfully.")

joblib.dump(
   {
       "model": model,
       "feature_columns": X.columns.tolist(),
   },
   "models/isolation_forest.joblib",
)
print("Model saved to models/isolation_forest.joblib")