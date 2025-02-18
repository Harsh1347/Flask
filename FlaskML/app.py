from flask import Flask,render_template,request
import pandas as pd 
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',val = {"pred":""})

@app.route('/predict',methods = ['POST','GET'])
def predict():
    data = pd.read_csv("Salary_Data.csv")
    x = np.array(data['YearsExperience']).reshape(-1,1)
    lr = LinearRegression()
    lr.fit(x,np.array(data['Salary']))
    ex = [int(x) for x in request.form.values()]
    print(ex)
    ex = np.array(ex).reshape(1,-1) #CHANGE EX !!!!!!!
    pred = lr.predict(ex)[0]
    op = f"Your Expected Salary is Rs.{round(pred)}"

    return render_template('index.html', val = {"pred":op})

if __name__ == "__main__":
    app.run(debug=True)