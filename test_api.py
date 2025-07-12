from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model and expected column structure
model = joblib.load(os.path.join("models", "alert_classifier.pkl"))
expected_columns = joblib.load(os.path.join("models", "expected_columns.pkl"))

# Preprocess input to match training format
def preprocess_input(data):
    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)

    # Align columns
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)
    return input_df

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        input_df = preprocess_input(data)
        prediction = model.predict(input_df)[0]
        result = "true_positive" if prediction == 1 else "false_positive"
        return jsonify({"prediction": result})
    except Exception as e:
        print("❌ INTERNAL ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5050, debug=True)
