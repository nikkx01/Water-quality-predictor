import os
import pickle
import streamlit as st
import numpy as np

# Load model using absolute path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "rf_model.pkl")
model = pickle.load(open(model_path, "rb"))

# Title
st.title("💧 Water Quality Predictor")
st.markdown("Predict whether water is **Safe or Unsafe** using Machine Learning.")

st.markdown("---")

# Input fields (with realistic default values)
aluminium = st.number_input("Aluminium", value=1.5)
ammonia = st.number_input("Ammonia", value=10.0)
arsenic = st.number_input("Arsenic", value=0.05)
barium = st.number_input("Barium", value=2.5)
cadmium = st.number_input("Cadmium", value=0.005)
chloramine = st.number_input("Chloramine", value=5.0)
chromium = st.number_input("Chromium", value=0.5)
copper = st.number_input("Copper", value=0.5)
flouride = st.number_input("Flouride", value=0.5)
bacteria = st.number_input("Bacteria", value=0.0)
viruses = st.number_input("Viruses", value=0.0)
lead = st.number_input("Lead", value=0.05)
nitrates = st.number_input("Nitrates", value=5.0)
nitrites = st.number_input("Nitrites", value=1.0)
mercury = st.number_input("Mercury", value=0.005)
perchlorate = st.number_input("Perchlorate", value=30.0)
radium = st.number_input("Radium", value=5.0)
selenium = st.number_input("Selenium", value=0.05)
silver = st.number_input("Silver", value=0.3)
uranium = st.number_input("Uranium", value=0.02)

st.markdown("---")

# Prediction
if st.button("Predict"):
    input_data = np.array([[ 
        aluminium, ammonia, arsenic, barium, cadmium,
        chloramine, chromium, copper, flouride, bacteria,
        viruses, lead, nitrates, nitrites, mercury,
        perchlorate, radium, selenium, silver, uranium
    ]])

    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)

    confidence = max(proba[0]) * 100

    if prediction[0] == 1:
        st.success("✅ Water is Safe")
    else:
        st.error("❌ Water is Not Safe")

    st.info(f"Confidence: {confidence:.2f}%")

# Footer
st.markdown("---")
st.markdown("### About")
st.write("This project uses a Random Forest model trained on water quality parameters to predict water safety.")