# AI and Data Documentation
## Prediction Model Documentation 

## Overview
This Python script contains code for developing a machine learning model to detect heart disease based on a given dataset. The model leverages various Python libraries for data preprocessing, feature engineering, model training, and evaluation.

## Purpose
The purpose of this model is to predict the presence or absence of heart disease in individuals based on a set of features. Early detection of heart disease can significantly improve patient outcomes by enabling timely interventions and treatments.

## Dataset 
### Dataset Description:

#### Variable Description

- **age**: Age of the patient in years

- **sex**: Gender of the patient (0 = male, 1 = female)

- **cp**: Chest pain type:
    - 0: Typical angina
    - 1: Atypical angina
    - 2: Non-anginal pain
    - 3: Asymptomatic

- **trestbps**: Resting blood pressure in mm Hg

- **chol**: Serum cholesterol in mg/dl

- **fbs**: Fasting blood sugar level, categorized as above 120 mg/dl (1 = true, 0 = false)

- **restecg**: Resting electrocardiographic results:
    - 0: Normal
    - 1: Having ST-T wave abnormality
    - 2: Showing probable or definite left ventricular hypertrophy

- **thalach**: Maximum heart rate achieved during a stress test

- **exang**: Exercise-induced angina (1 = yes, 0 = no)

- **oldpeak**: ST depression induced by exercise relative to rest

- **slope**: Slope of the peak exercise ST segment:
    - 0: Upsloping
    - 1: Flat
    - 2: Downsloping

- **ca**: Number of major vessels (0-4) colored by fluoroscopy

- **thal**: Thallium stress test result:
    - 0: Normal
    - 1: Fixed defect
    - 2: Reversible defect
    - 3: Not described

- **target**: Heart disease status (0 = no disease, 1 = presence of disease)
