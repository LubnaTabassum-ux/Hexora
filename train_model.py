import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Training data
data = [
   {"event_type": "PORT_SCAN", "device_type": "firewall", "severity": "low", "label": 0},
    {"event_type": "PORT_SCAN", "device_type": "router", "severity": "high", "label": 1},
    {"event_type": "PORT_SCAN", "device_type": "router", "severity": "medium", "label": 0},
    {"event_type": "FAILED_LOGIN", "device_type": "ids", "severity": "medium", "label": 0},
    {"event_type": "FAILED_LOGIN", "device_type": "siem", "severity": "high", "label": 1},
    {"event_type": "FAILED_LOGIN", "device_type": "firewall", "severity": "low", "label": 0},
    {"event_type": "MALWARE", "device_type": "endpoint", "severity": "high", "label": 1},
    {"event_type": "MALWARE", "device_type": "firewall", "severity": "medium", "label": 1},
    {"event_type": "MALWARE", "device_type": "router", "severity": "low", "label": 0},
    {"event_type": "MALWARE", "device_type": "ids", "severity": "high", "label": 1},
    {"event_type": "DDoS", "device_type": "firewall", "severity": "high", "label": 1},
    {"event_type": "DDoS", "device_type": "router", "severity": "medium", "label": 1},
    {"event_type": "DDoS", "device_type": "ids", "severity": "low", "label": 0},
    {"event_type": "DATA_EXFILTRATION", "device_type": "siem", "severity": "high", "label": 1},
    {"event_type": "DATA_EXFILTRATION", "device_type": "firewall", "severity": "medium", "label": 1},
    {"event_type": "DATA_EXFILTRATION", "device_type": "router", "severity": "low", "label": 0},
    {"event_type": "PORT_SCAN", "device_type": "endpoint", "severity": "low", "label": 0},
    {"event_type": "FAILED_LOGIN", "device_type": "endpoint", "severity": "medium", "label": 1},
    {"event_type": "MALWARE", "device_type": "siem", "severity": "medium", "label": 1},
    {"event_type": "DDoS", "device_type": "endpoint", "severity": "high", "label": 1},
    {"event_type": "DATA_EXFILTRATION", "device_type": "ids", "severity": "high", "label": 1}
]

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

# Define categorical columns
categorical_features = ["event_type", "device_type", "severity"]

# Create a preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Create full pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier())
])

# Train pipeline
pipeline.fit(X, y)

# Save full pipeline model
model_path = os.path.join("models", "alert_classifier.pkl")
joblib.dump(pipeline, model_path)
print(f"✅ Pipeline model saved to {model_path}")
