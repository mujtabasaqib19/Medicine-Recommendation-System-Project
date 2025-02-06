# Medicine Recommendation System Project

## Overview
This project provides information on diseases, including recommended medications, descriptions, precautions, workouts, and dietary suggestions. Users can enter the name of a disease, and the system will return relevant details while also handling minor spelling errors in disease names.

## Features
- Corrects minor spelling mistakes in disease names using approximate string matching.
- Retrieves medications for a given disease.
- Provides a brief description of the disease.
- Lists recommended precautions.
- Suggests workouts related to the disease.
- Recommends diets for better management of the disease.

## Data Files
The project uses several CSV files as data sources:
- `precautions_df.csv` - Contains precautionary measures for diseases.
- `workout_df.csv` - Lists recommended workouts for different diseases.
- `description.csv` - Provides brief descriptions of diseases.
- `medications.csv` - Contains medications associated with diseases.
- `diets.csv` - Lists recommended diets for specific diseases.
- `symtoms_df.csv` - (Not used in the main script but can be expanded for symptom-based disease identification.)

## Dependencies
Ensure you have the following Python packages installed before running the script:
```bash
pip install pandas numpy difflib
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/medicine-recommendation-system.git
   cd medicine-recommendation-system
   ```
2. Place the CSV data files in the project directory.
3. Install the required dependencies (as shown above).

## Usage
Run the script using:
```bash
python medicine_recommendation.py
```
Enter a disease name when prompted, and the system will display the corresponding information, including medications, descriptions, precautions, workouts, and diets.

### Example Usage:
```bash
Enter your disease: diabtes
```
Output:
```
Recommended Medicines for: diabetes

Medications:
1. Metformin
2. Insulin

Description: Diabetes is a chronic condition that affects blood sugar regulation.

Precautions:
1. Maintain a balanced diet.
2. Regularly monitor blood sugar levels.
3. Exercise daily.
4. Stay hydrated.

Workout Recommendations:
1. Walking
2. Yoga
3. Light Strength Training

Diet Recommendations:
1. High-fiber foods
2. Low-carb meals
3. Leafy green vegetables
```

## Future Enhancements
- Implement symptom-based disease prediction.
- Develop a web-based or mobile application for user-friendly interaction.
- Enhance disease name correction using advanced NLP techniques.
- Provide alternative medication options.

## Deployment Link
[This project is open-source under the MIT License.]
(https://medicine-recommendation-system-project.onrender.com)

## Author
Mujtaba Saqib

Feel free to contribute or suggest improvements!

