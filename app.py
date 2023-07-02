from flask import Flask, request, render_template, jsonify 
import pickle
import pandas as pd
import numpy as np
import joblib
app = Flask(__name__)

output = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    creditScore = int(request.form['creditScore'])
    geography = request.form['geography']
    gender = request.form['gender']
    age = int(request.form['age'])
    tenure = int(request.form['tenure'])
    balance = float(request.form['balance'])
    numOfProducts = int(request.form['numOfProducts'])
    hasCrCard = int(request.form['hasCrCard'])
    isActiveMember = int(request.form['isActiveMember'])
    estimatedSalary = float(request.form['estimatedSalary'])
    complain = int(request.form['complain'])
    satisfactionScore = int(request.form['satisfactionScore'])
    cardType = request.form['cardType']
    pointsEarned = int(request.form['pointsEarned'])

    with open('encoded_values.pkl', 'rb') as file:
        mapping_dict = pickle.load(file)

    geography = mapping_dict['Geography'][geography]
    cardType = mapping_dict['Card Type'][cardType]
    gender = mapping_dict['Gender'][gender]

    input_dict = {
        'CreditScore': creditScore,
        'Geography' : geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts':numOfProducts,
        'HasCrCard': hasCrCard,
        'IsActiveMember': isActiveMember,
        'EstimatedSalary': estimatedSalary,
        'Complain': complain,
        'Satisfaction Score': satisfactionScore,
        'Card Type': cardType,
        'Point Earned': pointsEarned
    }

    input_df = pd.DataFrame([input_dict])

    scaler = joblib.load('scaler.bin')
    input_array = scaler.transform(input_df)

    with open('model_8_16_1.pkl', 'rb') as f:
        model = pickle.load(f)

    predictions = model.predict(input_array)
    interpretation = np.where(predictions > 0.5, 1, 0)
    output = "The customer is predicted to " + ("leave" if interpretation == 1 else "stay")
    print(output)

    return jsonify(content=output)

if __name__ == '__main__':
    app.run()