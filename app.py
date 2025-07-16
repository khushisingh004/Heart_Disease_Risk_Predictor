import streamlit as st
import numpy as np
import joblib

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="Heart Disease Risk Predictor", layout="centered")

# -------------------- INLINE STYLING --------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;  /* Light gray background */
    }
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #d63384;  /* Pink-purple title */
        text-align: center;
        padding-top: 20px;
    }
    .subtext {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- TITLE SECTION --------------------
st.markdown('<div class="main-title">💓 Heart Disease Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">This tool predicts your heart disease risk based on your medical data.</div>', unsafe_allow_html=True)
st.markdown("---")

# -------------------- LOAD MODEL --------------------
model = joblib.load('C:\\Users\\khush\\models\\logistic_model.pkl')
scaler = joblib.load('C:\\Users\\khush\\models\\scaler.pkl')

# -------------------- SIDEBAR --------------------
st.sidebar.header("📝 Patient Information")

age = st.sidebar.number_input("Age", 20, 100)
sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.sidebar.number_input("Resting Blood Pressure", 80, 200)
chol = st.sidebar.number_input("Cholesterol (mg/dl)", 100, 400)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.sidebar.selectbox("Resting ECG", [0, 1, 2])
thalach = st.sidebar.number_input("Max Heart Rate", 60, 220)
exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.sidebar.number_input("ST Depression", 0.0, 6.0, step=0.1)
slope = st.sidebar.selectbox("Slope of ST Segment", [0, 1, 2])
ca = st.sidebar.selectbox("Number of Major Vessels", [0, 1, 2, 3])
thal = st.sidebar.selectbox("Thalassemia", [0, 1, 2])

# -------------------- ENCODING --------------------
cp_1, cp_2, cp_3 = int(cp == 1), int(cp == 2), int(cp == 3)
thal_1, thal_2 = int(thal == 1), int(thal == 2)
slope_1, slope_2 = int(slope == 1), int(slope == 2)

input_data = np.array([[age, sex, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, ca,
                        cp_1, cp_2, cp_3,
                        thal_1, thal_2,
                        slope_1, slope_2]])

input_scaled = scaler.transform(input_data)

# -------------------- PREDICTION --------------------
if st.button("💡 Predict Risk"):
    result = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if result == 1:
        st.error("🚨 **High Risk of Heart Disease!**")
        st.markdown(f"🩺 **Probability of Risk:** `{prob:.2f}`")
    else:
        st.success("✅ **Low Risk of Heart Disease.**")
        st.markdown(f"🩺 **Probability of Risk:** `{prob:.2f}`")
        st.balloons()

# -------------------- FOOTER --------------------
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
