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
@app.route("/predict", methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        Visit=int(request.form['Visit'])
        MR Delay=int(request.form['MR Delay'])
        Gender=request.form['Gender']
        Age=int(request.form['Age'])
        SES=request.form['SES']
        CDR=request.form['CDR']
        Gender=request.form['Gender']
        Visit=request.form['Visit']
    

        prediction=model.predict([[Visit, MR Delay, M/F, Age, EDUC, SES, MMSE, CDR, eTIV, nWBV, ASF]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',pred="I am afraid you are at risk of dementia")
        else:
            return render_template('index.html',pred="Congratulations, you are not at risk of dementia! {}".format(output))
    else:
        return render_template('index.html', pred= 'Enter Correct Details')

if __name__=="__main__":
    app.run(debug=True)

