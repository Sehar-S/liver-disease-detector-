import streamlit as st
import pandas as pd
import joblib
import time

# Load model, scaler, columns
model = joblib.load('liver_model.pkl')
scaler = joblib.load('liver_scaler.pkl')
model_columns = joblib.load('liver_columns.pkl')

st.set_page_config(page_title="Liver Disease Detector", page_icon="🩺", layout="centered")

# ---------- CUSTOM CSS (Teal / Medical Dark Theme) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #041014, #06232b, #0a2f38, #0d3b45);
    background-size: 400% 400%;
    animation: gradientShift 18s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.title-container {
    text-align: center;
    padding: 25px 0 15px 0;
    animation: fadeInDown 1s ease-out;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

.main-title {
    font-size: 38px;
    font-weight: 700;
    background: linear-gradient(90deg, #2dd4bf, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}

.subtitle {
    color: #7fb3ad;
    font-size: 15px;
    margin-bottom: 10px;
}

.glass-card {
    background: rgba(20, 60, 60, 0.35);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 26px;
    border: 1px solid rgba(45, 212, 191, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
    margin-bottom: 20px;
    animation: fadeInUp 0.8s ease-out;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.section-label {
    color: #2dd4bf;
    font-weight: 600;
    font-size: 15px;
    margin-bottom: 12px;
}

div.stButton > button {
    background: linear-gradient(90deg, #2dd4bf, #67e8f9);
    color: #041014;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    padding: 13px 30px;
    font-size: 16px;
    width: 100%;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(45, 212, 191, 0.5);
}

.result-box {
    text-align: center;
    padding: 28px;
    border-radius: 18px;
    animation: popIn 0.5s ease-out;
    margin-top: 15px;
}

@keyframes popIn {
    0% { opacity: 0; transform: scale(0.85); }
    100% { opacity: 1; transform: scale(1); }
}

.result-disease { background: rgba(255, 82, 82, 0.12); border: 1px solid rgba(255, 82, 82, 0.4); }
.result-nodisease { background: rgba(45, 212, 191, 0.12); border: 1px solid rgba(45, 212, 191, 0.4); }

.result-text {
    font-size: 28px;
    font-weight: 700;
    color: #f0f4fa;
}

.result-sub {
    color: #7fb3ad;
    font-size: 14px;
    margin-top: 6px;
}

label, .stSlider label, .stSelectbox label, .stNumberInput label {
    color: #cfe8e4 !important;
    font-weight: 500 !important;
    font-size: 14px !important;
}

.stSlider [data-baseweb="slider"] > div > div {
    background: linear-gradient(90deg, #2dd4bf, #67e8f9) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("""
<div class="title-container">
    <div class="main-title">🩺 Liver Disease Detector</div>
    <div class="subtitle">AI-powered liver health assessment based on blood test values</div>
</div>
""", unsafe_allow_html=True)

# ---------- INPUT CARD ----------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Patient Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 4, 90, 40)
    gender = st.selectbox("Gender", ["Male", "Female"])
    total_bilirubin = st.number_input("Total Bilirubin (mg/dL)", 0.1, 75.0, 1.0, step=0.1)
    direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", 0.1, 20.0, 0.3, step=0.1)
    alkaline_phosphotase = st.number_input("Alkaline Phosphotase (IU/L)", 60, 2200, 200)
with col2:
    alamine_aminotransferase = st.number_input("ALT / Alamine Aminotransferase (IU/L)", 10, 2000, 30)
    aspartate_aminotransferase = st.number_input("AST / Aspartate Aminotransferase (IU/L)", 10, 5000, 35)
    total_proteins = st.number_input("Total Proteins (g/dL)", 2.0, 10.0, 6.8, step=0.1)
    albumin = st.number_input("Albumin (g/dL)", 0.5, 6.0, 3.3, step=0.1)
    ag_ratio = st.number_input("Albumin and Globulin Ratio", 0.1, 3.0, 1.0, step=0.1)

st.markdown("<br>", unsafe_allow_html=True)
predict_btn = st.button("Analyze Liver Health")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- PREDICTION ----------
if predict_btn:
    with st.spinner("Analyzing blood test values..."):
        time.sleep(0.8)

        input_dict = {
            'Age': age,
            'Gender': 1 if gender == 'Male' else 0,
            'Total_Bilirubin': total_bilirubin,
            'Direct_Bilirubin': direct_bilirubin,
            'Alkaline_Phosphotase': alkaline_phosphotase,
            'Alamine_Aminotransferase': alamine_aminotransferase,
            'Aspartate_Aminotransferase': aspartate_aminotransferase,
            'Total_Protiens': total_proteins,
            'Albumin': albumin,
            'Albumin_and_Globulin_Ratio': ag_ratio,
        }

        input_df = pd.DataFrame([input_dict])
        input_df = input_df[model_columns]

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]

    style_class = "result-disease" if prediction == "Disease" else "result-nodisease"
    result_label = "Liver Disease Detected" if prediction == "Disease" else "No Liver Disease Detected"

    st.markdown(f"""
    <div class="result-box {style_class}">
        <div class="result-text">{result_label}</div>
        <div class="result-sub">Based on the provided blood test values</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    prob_df = pd.DataFrame({'Status': model.classes_, 'Probability': probabilities})
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Confidence Breakdown</div>', unsafe_allow_html=True)
    st.bar_chart(prob_df.set_index('Status'))
    st.markdown('</div>', unsafe_allow_html=True)

    if prediction == "Disease":
        st.error("This result suggests abnormal liver markers. Please consult a healthcare professional for further testing and diagnosis.")
    else:
        st.success("Your liver markers appear within a typical range. Regular checkups are still recommended for ongoing health monitoring.")

    st.caption("Disclaimer: This tool is for educational purposes only and does not substitute professional medical advice.")
