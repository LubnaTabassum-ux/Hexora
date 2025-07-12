from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load full pipeline model
model_path = os.path.join("models", "alert_classifier.pkl")
model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input provided"}), 400

        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)[0]
        result = "true_positive" if prediction == 1 else "false_positive"

        return jsonify({"prediction": result})

    except Exception as e:
        print("❌ INTERNAL ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5050, debug=True)
