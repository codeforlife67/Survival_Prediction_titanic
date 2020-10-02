from flask import Flask
import json
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "hello world"

#http://127.0.0.1:5000/titanic/1/0/22/0/0/150/0
@app.route("/titanic/<pclass>/<sex>/<age>/<sibsp>/<parch>/<fare>/<embarked>")
def predict_survival(pclass,sex,age,sibsp,parch,fare,embarked):
    pclass,sex,age,sibs,parch,fare,embarked = int(pclass),int(sex),int(age),int(sibsp),int(parch),int(fare),int(embarked)    
    input_test = [[pclass,sex,age,sibs,parch,fare,embarked]]
    my_survival_scaled = sc.fit_transform(input_test)
    model = pickle.load(open("survival_prediction.sav","rb"))
    pred = model.predict(my_survival_scaled)
    if pred == 0 :
       pred_response = "you died on titanic"
    else :
         pred_response = "you survived on titanic"
    #pred = str(pred[0]) this is string return type 
    return jsonify(prediction=float(pred[0]),
                   prediction_response = pred_response)

if __name__ == "__main__":
    sc = StandardScaler()
    app.run(debug=True)
    
