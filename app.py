# app.py

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('saved_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form.get(key)) for key in ['pktcount', 'bytecount', 'pktrate', 'flows', 'Protocol']]
        data = scaler.transform([data])
        prediction = model.predict(data)[0]

        result = "🚨 DDoS Attack Detected!" if prediction == 1 else "✅ Normal Traffic (Safe)"
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text="❌ Invalid Input")

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
    app.run(debug=True)
