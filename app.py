from flask import Flask, jsonify, request
import pandas as pd
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Funzione per generare dati
def generate_data(num_records):
    data = []
    diagnoses = ["Healthy", "Diabetes", "Hypertension", "Pre-Diabetes", "Obesity"]
    genders = ["Male", "Female"]
    for i in range(1, num_records + 1):
        systolic = random.randint(110, 180)
        diastolic = random.randint(70, 120)
        glucose_level = random.randint(70, 250)
        glucose_category = (
            "Normal" if glucose_level < 100 
            else "Pre-Diabetic" if glucose_level < 140 
            else "Diabetic"
        )
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

# Endpoint principale per generare dati
@app.route('/generate', methods=['GET'])
def generate_endpoint():
    try:
        num_records = int(request.args.get('num_records', 100))
        if num_records > 100000:
            return jsonify({"error": "Max limit of 100,000 records exceeded."}), 400
        
        data = generate_data(num_records)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
