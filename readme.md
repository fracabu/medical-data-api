# 🏥 Medical Data API

> API Flask per la generazione di dati medici simulati, deployata su Render.

## 🔗 Link API
**URL Base**: `https://medical-data-api-2.onrender.com`  
**Endpoint Disponibile**: `/generate`

## 📋 Descrizione

Questa API genera dataset simulati di pazienti con varie metriche mediche, inclusi:
- Pressione sanguigna
- Livelli di glucosio
- Diagnosi
- Dati demografici

## 🚀 Endpoint

### Generate Random Medical Data
```http
GET /generate?num_records={number}
```

**URL Completo di Esempio:**
```
https://medical-data-api-2.onrender.com/generate?num_records=100
```

**Parametri Query:**
- `num_records` (opzionale): Numero di record da generare (default: 100, max: 100,000)

**Response Format**: JSON

## 📊 Struttura dei Dati

Ogni record contiene i seguenti campi:
```json
{
    "ID": 1,
    "Name": "Patient_1",
    "Age": 45,
    "Gender": "Female",
    "Diagnosis": "Healthy",
    "BloodPressure": "120/80",
    "Systolic": 120,
    "Diastolic": 80,
    "GlucoseLevel": 95,
    "GlucoseCategory": "Normal",
    "VisitDate": "2024-11-27"
}
```

### Ranges e Categorie:
- **Age**: 18-80 anni
- **Gender**: Male/Female
- **Diagnosis**: Healthy, Diabetes, Hypertension, Pre-Diabetes, Obesity
- **Blood Pressure**: 
  - Systolic: 110-180 mmHg
  - Diastolic: 70-120 mmHg
- **Glucose Level**: 70-250 mg/dL
  - Normal: < 100 mg/dL
  - Pre-Diabetic: 100-139 mg/dL
  - Diabetic: ≥ 140 mg/dL

## 💻 Esempi di Utilizzo

### Python con Requests
```python
import requests
import pandas as pd

# Genera 100 record
response = requests.get("https://medical-data-api-2.onrender.com/generate?num_records=100")
data = response.json()

# Converti in DataFrame
df = pd.DataFrame(data)
```

### JavaScript/Fetch
```javascript
fetch('https://medical-data-api-2.onrender.com/generate?num_records=100')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## ⚠️ Limiti
- Massimo 100,000 record per richiesta
- API gratuita con limiti di rate su Render
- Dati generati casualmente per scopi dimostrativi
- L'istanza gratuita su Render può andare in sleep dopo periodi di inattività, causando un ritardo nella prima richiesta

## 🔒 Note sulla Sicurezza
- I dati sono simulati e non contengono informazioni personali reali
- Non utilizzare per scopi medici o diagnostici reali
- API pubblica senza autenticazione

## 📝 Note di Sviluppo
- Implementata con Flask
- Deployata su Render
- Genera dati casuali ma realistici
- Supporta CORS per utilizzo frontend

## 🤝 Contributi
Per suggerimenti o problemi, apri una issue su GitHub o contatta il team di sviluppo.

---
Sviluppato con ❤️ per scopi didattici e dimostrativi.