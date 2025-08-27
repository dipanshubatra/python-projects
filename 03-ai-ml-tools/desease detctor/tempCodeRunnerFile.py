import pandas as pd
import joblib

model = joblib.load("stoke_predictore.pkl")

print("\nEnter Patient Details:")

data = {
    "id": int(input("ID (any number): ")),
    "gender": int(input("Gender (0=Female, 1=Male, 2=Other): ")),
    "age": float(input("Age: ")),
    "hypertension": int(input("Hypertension (0=No, 1=Yes): ")),
    "heart_disease": int(input("Heart Disease (0=No, 1=Yes): ")),
    "ever_married": int(input("Ever Married (0=No, 1=Yes): ")),
    "work_type": int(input("Work Type (0=Govt_job, 1=Never_worked, 2=Private, 3=Self-employed, 4=children): ")),
    "Residence_type": int(input("Residence Type (0=Rural, 1=Urban): ")),
    "avg_glucose_level": float(input("Average Glucose Level: ")),
    "bmi": float(input("BMI: ")),
    "smoking_status": int(input("Smoking Status (0=Unknown, 1=formerly smoked, 2=never smoked, 3=smokes): "))
}

new_data = pd.DataFrame([data])

prediction = model.predict(new_data)[0]

if prediction == 1:
    print("\n⚠️ The model predicts: STROKE RISK")
else:
    print("\n✅ The model predicts: NO STROKE RISK")
