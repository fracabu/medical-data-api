import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# Funzione per generare dati
def generate_data(num_records):
    data = []
    diagnoses = ["Healthy", "Diabetes", "Hypertension", "Pre-Diabetes", "Obesity"]
    genders = ["Male", "Female"]
    for i in range(1, num_records + 1):
        systolic = random.randint(110, 180)
        diastolic = random.randint(70, 120)
        glucose_level = random.randint(70, 250)
        glucose_category = "Normal" if glucose_level < 100 else "Pre-Diabetic" if glucose_level < 140 else "Diabetic"
        record = {
            "ID": i,
            "Name": f"Patient_{i}",
            "Age": random.randint(18, 80),
            "Gender": random.choice(genders),
            "Diagnosis": random.choice(diagnoses),
            "BloodPressure": f"{systolic}/{diastolic}",
            "Systolic": systolic,
            "Diastolic": diastolic,
            "GlucoseLevel": glucose_level,
            "GlucoseCategory": glucose_category,
            "VisitDate": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        }
        data.append(record)
    return data

# Streamlit app
st.title("Medical Data API")

# Input per il numero di record
num_records = st.number_input("Number of records to generate", min_value=1, max_value=100000, value=100)

# Generazione dei dati
if st.button("Generate Data"):
    data = generate_data(num_records)
    df = pd.DataFrame(data)
    st.write("Generated Data:")
    st.dataframe(df)

    # Download CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="medical_data.csv", mime="text/csv")
