# 🩺 Disease Prediction using Machine Learning

This project is a **Machine Learning-based Disease Prediction Tool** that predicts the risk of stroke based on patient health attributes like age, BMI, hypertension, heart disease, smoking status, and more. The model uses **Logistic Regression** with a full ML pipeline.

---

## 🚀 Features
- Handles missing values automatically with `SimpleImputer`
- Encodes categorical features
- Scales numeric features using `StandardScaler`
- Trains a **Logistic Regression** model
- Performs **GridSearchCV** to optimize hyperparameters
- Provides real-time user input for prediction
- Prints model **accuracy** and **classification report**

---

## 📂 Project Structure
disease-prediction/
│── train.py # Train the ML model and save pipeline
│── predict.py # Take user input and predict stroke risk
│── healthcare-dataset-stroke-data.csv # Dataset for training
│── stroke_predictor.pkl # Saved trained model (auto-generated)
│── README.md # Project documentation

---

## ⚙️ Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/disease-prediction.git
cd disease-prediction
Install dependencies:
pip install pandas scikit-learn joblib
▶️ How to Run

Train the model:

python train.py


Predict using user input:

python predict.py
