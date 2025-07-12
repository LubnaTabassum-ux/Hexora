# Hexora
This project aims to enhance IT security operations by leveraging machine learning and intelligent filtering to significantly reduce false positives in security alerts. By analyzing patterns in alert data, historical logs, and contextual signals, the system helps security teams prioritize real threats and reduce alert fatigue.

# Intelligent Security Alert Classifier
**Team: Hexora**  
**Hackathon: SG Hackathon 2026**  
**Category: Intelligent IT Operations – Reducing False Positives in Security Alerts**

## Problem Statement
Modern IT environments generate an overwhelming number of logs and alerts. Many are false positives due to outdated rules or lack of contextual awareness, leading to alert fatigue and missed threats.

## Solution Overview
Our system intelligently classifies security alerts from network devices into true or false positives using:
- A trained ML model via a Flask API backend
- A real-time, animated Streamlit dashboard frontend
- Risk-level visualization and alert confidence scoring
- Real-time prediction logging + explainability placeholders

## Tech Stack
- Python, Flask, Streamlit, scikit-learn
- HTML/CSS animation via Streamlit markdown
- Matplotlib, pandas, joblib, fpdf

## Key Features
- 🔮 AI-based alert classification (true vs. false positives)
- 📶 Risk-level meter + animated confidence gauge
- 💾 Logging to CSV (`prediction_log.csv`)
- 📊 Chart of prediction types by severity
- 📈 Explainability placeholders for model understanding
- 🎨 Cybersecurity-themed dark UI with custom background
- 🧑‍💻 Team branding & project identity

## Project Structure
```
flask-test/
├── backend/
│   ├── app.py
│   └── models/
│       └── alert_classifier.pkl
├── frontend/
│   ├── streamlit_app.py
│   └── images/
│       └── cyber.jpg
├── models/
│   └── train_model.py
├── prediction_log.csv
├── prediction_chart.png
└── README.md
```

## How to Run

### 1. 🔧 Backend (Flask API)
```bash
cd backend
python app.py
```

### 2. Frontend (Streamlit Dashboard)
```bash
cd frontend
streamlit run streamlit_app.py
```

## Unique Features of Hexora's Solution

### 🔮 1. Context-Aware False Positive Reduction
Unlike traditional SIEMs that rely on rigid rule-based filtering, Hexora uses ML trained on contextual and behavioral data to reduce false positives intelligently.

### 🚦 2. Real-Time Risk-Level Visualization
We go beyond binary classifications — each alert displays a confidence score and dynamic visual risk meter to assist analysts in making faster decisions.

### 📊 3. Alert Logging + Explainability Framework
The system not only logs predictions with metadata (severity, type, device), but also includes placeholders to integrate model interpretability (e.g., SHAP, LIME).

### 🎨 4. Fully Branded, Animated Dashboard
Modern UI with cyber-themed visuals, animated pulse effects, confidence bars, and team branding — far more engaging than standard security UIs.

### 🔁 5. Self-Learning System Ready
The architecture supports adding analyst feedback for continuous retraining, enabling adaptive threat intelligence.


**Developed by Team Hexora** | SG Hackathon 2026  
For queries, contact via GitHub or team email.

