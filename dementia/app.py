from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Visit=float(request.form['Visit'])
        MR Delay=int(request.form['MR Delay'])
        Gender=request.form['Gender']
        Age=int(request.form['Age'])
        SES=request.form['SES']
        if(SES=='Yes'):
                Once=1
                Twice=2
                Thrice=3
                Four_Times=4
                Five_Times=5
        else:
            None=0

        CDR=request.form['CDR']
        if(CDR=='Yes'):
                Half= 0.5
                Once=1
                Twice=2
                Thrice=3
                
        else:
            None=0
            

        Gender=request.form['Gender']
        if(Gender=='Yes'):
            Malel=1
        else:
            Female=0

        Visit=request.form['Visit']
        if(Visit=='Yes'):
            Once=1
            Twice=0
            Thrice=3
            Four_Times=4
            Five_Times=5

        else:
            TVisit=0

        prediction=model.predict([[Visit, MR Delay, M/F, Age, EDUC, SES, MMSE, CDR, eTIV, nWBV, ASF]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="I am afraid you are at risk of dementia")
        else:
            return render_template('index.html',prediction_text="Congratulations, you are not at risk of dementia! {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

