import os
import pickle
import streamlit as st
import numpy as np

# Get absolute path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "rf_model.pkl")

# Load model
model = pickle.load(open(model_path, "rb"))

st.title("💧 Water Quality Predictor")

st.write("Enter water parameters:")

# Input fields
aluminium = st.number_input("Aluminium")
ammonia = st.number_input("Ammonia")
arsenic = st.number_input("Arsenic")
barium = st.number_input("Barium")
cadmium = st.number_input("Cadmium")
chloramine = st.number_input("Chloramine")
chromium = st.number_input("Chromium")
copper = st.number_input("Copper")
flouride = st.number_input("Flouride")
bacteria = st.number_input("Bacteria")
viruses = st.number_input("Viruses")
lead = st.number_input("Lead")
nitrates = st.number_input("Nitrates")
nitrites = st.number_input("Nitrites")
mercury = st.number_input("Mercury")
perchlorate = st.number_input("Perchlorate")
radium = st.number_input("Radium")
selenium = st.number_input("Selenium")
silver = st.number_input("Silver")
uranium = st.number_input("Uranium")

# Predict button
if st.button("Predict"):
    input_data = np.array([[aluminium, ammonia, arsenic, barium, cadmium,
                            chloramine, chromium, copper, flouride, bacteria,
                            viruses, lead, nitrates, nitrites, mercury,
                            perchlorate, radium, selenium, silver, uranium]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Water is Safe")
    else:
        st.error("❌ Water is Not Safe")