import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Step 1: Training data
data = [
    {"event_type": "PORT_SCAN", "device_type": "firewall", "severity": "low", "label": 0},
    {"event_type": "FAILED_LOGIN", "device_type": "ids", "severity": "medium", "label": 0},
    {"event_type": "MALWARE", "device_type": "firewall", "severity": "high", "label": 1},
    {"event_type": "PORT_SCAN", "device_type": "router", "severity": "high", "label": 1},
    {"event_type": "FAILED_LOGIN", "device_type": "firewall", "severity": "low", "label": 0},
    {"event_type": "MALWARE", "device_type": "ids", "severity": "high", "label": 1}
]

df = pd.DataFrame(data)

# Step 2: One-hot encode input
X = pd.get_dummies(df.drop("label", axis=1))
y = df["label"]

# Step 3: Save expected column names
expected_columns = X.columns.tolist()
columns_path = os.path.join("models", "expected_columns.pkl")
joblib.dump(expected_columns, columns_path)

# Step 4: Train model
model = RandomForestClassifier()
model.fit(X, y)

# Step 5: Save model
model_path = os.path.join("models", "alert_classifier.pkl")
joblib.dump(model, model_path)

# ✅ Done
print("✅ Model trained and saved to", model_path)
print("✅ Columns saved to", columns_path)
