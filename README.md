# 🩺 Liver Disease Detector

An AI-powered web application that predicts the likelihood of liver disease based on patient blood test values. Built as part of a machine learning project series exploring different algorithms across healthcare use cases.

🔗 **Live App:** https://bcy6ujtqm7da5g5vv8tnnp.streamlit.app/

 "Note: This app is hosted on Streamlit Community Cloud's free tier. If the app appears inactive, please click 'Yes, get this app back up!' — it will load within a minute."
---

## What This Project Does

Liver disease is often detected through a blood test called a **Liver Function Test (LFT)**. This test measures several enzymes and proteins in the blood that indicate how well the liver is functioning.

This app takes a patient's LFT values as input and predicts whether the patient is likely to have liver disease or not, along with a confidence score for the prediction.

**Important:** This is an educational/academic project and is **not** a substitute for professional medical diagnosis. Always consult a doctor for actual health concerns.

---

## 🧬 Input Features Explained

| Feature | What It Means |
|---|---|
| **Age** | Age of the patient |
| **Gender** | Male / Female |
| **Total Bilirubin** | A pigment processed by the liver; high levels can indicate poor liver function (linked to jaundice) |
| **Direct Bilirubin** | The portion of bilirubin already processed by the liver |
| **Alkaline Phosphatase (ALP)** | An enzyme found in the liver and bones; elevated levels can signal liver damage |
| **Alamine Aminotransferase (ALT)** | A liver-specific enzyme; a key marker of liver cell damage |
| **Aspartate Aminotransferase (AST)** | A related enzyme found in the liver, heart, and muscles; used alongside ALT |
| **Total Proteins** | Total protein levels in the blood; a healthy liver produces adequate protein |
| **Albumin** | A specific protein produced only by the liver; low levels can indicate liver dysfunction |
| **Albumin/Globulin Ratio** | The ratio between albumin and other blood proteins; often disrupted in liver disease |

In simple terms: when liver cells are damaged, certain enzymes "leak" into the bloodstream and protein production drops. This model looks for those patterns in the blood test values to make its prediction.

---

## 🤖 Model Details

- **Algorithm:** Support Vector Machine (SVM) with a balanced class weighting to handle the imbalance between disease and non-disease cases in the dataset
- **Preprocessing:** Missing values imputed, categorical encoding for gender, feature scaling using StandardScaler (required for distance/margin-based models like SVM)
- **Dataset:** Indian Liver Patient Records (583 patient records, 10 clinical features)
- **Output:** Binary classification — *Disease* or *No Disease* — with prediction confidence

### Performance
- Balanced precision/recall across both classes using class-weighted SVM
- Evaluated using accuracy, precision, recall, F1-score, and confusion matrix

---

##  Tech Stack

- **Python**  data processing and model training
- **Scikit-learn**  SVM model, preprocessing, evaluation
- **Pandas**  data handling
- **Streamlit**  interactive web app interface
- **Joblib**   model serialization

---

##  Running Locally

```bash
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
```

Make sure `liver_model.pkl`, `liver_scaler.pkl`, and `liver_columns.pkl` are in the same folder as `app.py`.

---

## ⚠️ Disclaimer

This tool is built for educational purposes as part of a machine learning learning project. It should not be used for actual medical diagnosis or treatment decisions. Please consult a qualified healthcare professional for any health concerns.
