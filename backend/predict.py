import joblib

import pandas as pd

from services.feature_engineering import prepare_features

from services.risk_service import calculate_risk


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

X = prepare_features(df)

saved_model = joblib.load("models/isolation_forest.joblib")

model = saved_model["model"]

feature_columns = saved_model["feature_columns"]

X = X.reindex(columns=feature_columns, fill_value=0)

predictions = model.predict(X)

scores = model.decision_function(X)


results = pd.DataFrame({

    "prediction": predictions,

    "anomaly_score": scores,

})

results["status"] = results["prediction"].apply(

    lambda x: "Attack" if x == -1 else "Normal"

)

results["risk_level"] = results["anomaly_score"].apply(

    calculate_risk

)


print("\nFirst 10 predictions:")

print(results.head(10))


print("\nRisk level distribution:")

print(results["risk_level"].value_counts())
 