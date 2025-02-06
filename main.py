from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from difflib import get_close_matches

app = Flask(__name__)

# Load datasets
def load_data():
    data_files = {
        "precautions": "datasets/precautions_df.csv",
        "workout": "datasets/workout_df.csv",
        "description": "datasets/description.csv",
        "medications": "datasets/medications.csv",
        "diets": "datasets/diets.csv",
        "symptoms": "datasets/symtoms_df.csv"
    }
    return {key: pd.read_csv(value) for key, value in data_files.items()}

data = load_data()

# Extract diseases dynamically
all_diseases = data['medications']['Disease'].dropna().unique().tolist()

def correct_spelling(input_text, choices):
    match = get_close_matches(input_text, choices, n=1, cutoff=0.8)
    return match[0] if match else input_text

def fetch_medicine(disease):
    medicine_info = {}
    
    # Fetch medicines first
    medicine_info['medications'] = data['medications'].loc[
        data['medications']['Disease'] == disease, 'Medication'
    ].dropna().tolist()
    
    # If disease is found, fetch additional details
    if medicine_info['medications']:
        medicine_info['description'] = " ".join(data['description'].loc[
            data['description']['Disease'] == disease, 'Description'
        ].values)

        medicine_info['precautions'] = data['precautions'].loc[
            data['precautions']['Disease'] == disease, ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']
        ].dropna().values.tolist()

        medicine_info['workout'] = data['workout'].loc[
            data['workout']['disease'] == disease, 'workout'
        ].dropna().tolist()

        medicine_info['diets'] = data['diets'].loc[
            data['diets']['Disease'] == disease, 'Diet'
        ].dropna().tolist()
    
    return medicine_info

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_disease = request.form['disease']
        corrected_disease = correct_spelling(user_disease.lower(), all_diseases)
        medicine_info = fetch_medicine(corrected_disease)
        
        return render_template('index.html', disease=corrected_disease, info=medicine_info)
    
    return render_template('index.html', disease=None, info=None)

if __name__ == '__main__':
    app.run(debug=True)
