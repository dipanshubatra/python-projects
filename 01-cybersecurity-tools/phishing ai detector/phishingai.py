import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score,mean_squared_error,classification_report 
import joblib
data,meta = arff.loadarff("files/train_phish.arff")
df = pd.DataFrame(data)

if df["Result"].dtype == object:
    df["Result"] = df["Result"].astype(str)
df["Result"] = df["Result"].astype(int)
df["Result"] = df["Result"].map({-1:1,1:0})
x = df.drop("Result",axis=1)
y = df["Result"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("accruacy",r2_score(y_test,y_pred))
print("classification report",classification_report(y_test,y_pred))
joblib.dump(model,"phish_detector.pkl")
print("modelsaved")