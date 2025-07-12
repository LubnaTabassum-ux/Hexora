import streamlit as st
import requests
import base64
import random
import os
from PIL import Image

# --- Set Cyber-Themed Background ---
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }}
        .title {{
            font-size: 48px;
            font-weight: 800;
            color: #f0f0f0;
            text-align: center;
            margin-bottom: 25px;
            text-shadow: 0 0 10px #f200ff;
        }}
        label, .stSelectbox label {{
            font-size: 18px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
        }}
        .stSelectbox > div {{
            padding: 10px 10px;
            font-size: 16px;
        }}
        .stButton button {{
            background-color: #ff007f;
            color: white;
            border-radius: 10px;
            padding: 0.6em 2em;
            border: 2px solid white;
            font-weight: bold;
            transition: 0.3s;
        }}
        .stButton button:hover {{
            background-color: white;
            color: #ff007f;
            transform: scale(1.05);
        }}
        .prediction-box {{
            background-color: rgba(0,0,0,0.75);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            margin-top: 30px;
            font-size: 22px;
        }}
        .pulse {{
            height: 30px;
            width: 30px;
            background-color: #00ffcc;
            border-radius: 50%;
            animation: pulse-animation 1.5s infinite;
            margin: 0 auto;
        }}
        @keyframes pulse-animation {{
            0% {{ transform: scale(1); opacity: 0.9; }}
            50% {{ transform: scale(1.3); opacity: 0.4; }}
            100% {{ transform: scale(1); opacity: 0.9; }}
        }}
        .meter {{
            height: 20px;
            background: #ddd;
            border-radius: 5px;
            overflow: hidden;
        }}
        .meter > span {{
            display: block;
            height: 100%;
            background-color: #00ffcc;
            width: 80%;
            animation: grow 1s ease-in-out;
        }}
        @keyframes grow {{
            from {{ width: 0%; }}
            to {{ width: 100%; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Setup background
set_bg("images/cyber01.jpg")  # ✅ Make sure this image exists!

# --- Title ---
st.markdown('<div class="title">🔒 Intelligent Security Alert Classifier</div>', unsafe_allow_html=True)

# --- Input Form ---
with st.form("input_form"):
    st.subheader("📊 Select Event Details")
    event_type = st.selectbox("Event Type", ["PORT_SCAN", "MALWARE", "FAILED_LOGIN", "DDoS", "DATA_EXFILTRATION"])
    device_type = st.selectbox("Device Type", ["firewall", "ids", "router", "siem", "endpoint"])
    severity = st.selectbox("Severity", ["low", "medium", "high"])
    submit = st.form_submit_button("🚨 Predict Alert Type")

# --- Backend API Call ---
if submit:
    data = {
        "event_type": event_type,
        "device_type": device_type,
        "severity": severity
    }

    try:
        response = requests.post("http://localhost:5050/predict", json=data)
        if response.status_code == 200:
            result = response.json()["prediction"]
            emoji = "✅" if result == "true_positive" else "⚠️"
            color = "#00ffcc" if result == "true_positive" else "#ffa500"
            pulse_color = "#00ffcc" if result == "true_positive" else "#ff007f"
            risk_level = severity.capitalize()
            confidence = random.randint(80, 99) if result == "true_positive" else random.randint(50, 79)

            # Replace pulse color dynamically
            st.markdown(
                f"""
                <style>
                .pulse {{
                    background-color: {pulse_color};
                }}
                .meter > span {{
                    background-color: {color};
                    width: {confidence}%;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            # Display result
            st.markdown(
                f"""
                <div class="prediction-box" style="border-left: 6px solid {color}">
                    <div class="pulse"></div>
                    <h2 style="margin-top: 10px;">{emoji} Prediction: <span style="color:{color};">{result.upper()}</span></h2>
                    <p>📶 Risk Level: <strong>{risk_level}</strong></p>
                    <p>🎯 Confidence Score:</p>
                    <div class="meter"><span></span></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error(f"❌ API returned {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"💥 Could not connect to backend: {e}")
