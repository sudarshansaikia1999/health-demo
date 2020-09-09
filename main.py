import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pred')
def pred():
    return render_template('pred.html')

@app.route('/pred',methods=['GET','POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('pred.html', prediction_text='Employee Salary should be $ {}'.format(output))

    '''
    For rendering results on HTML GUI
    '''


if __name__ == "__main__":
    app.run(debug=True)