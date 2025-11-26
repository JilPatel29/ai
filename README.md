#Name: Jil Patel
#Enrollment: 250103002023

# DDoS Attack Detection Using Machine Learning

## 🚀 Project Overview
This project detects DDoS attacks using a machine learning model (Random Forest).  
It provides a web interface using Flask where users enter network traffic values to detect attacks.

## 🧠 Key Features
- Train ML model on SDN Dataset
- Flask web app for real-time prediction
- Only 5 inputs required
- RandomForest model used

## 📂 Project Structure
project_folder/
├── app.py
├── train_model.py
├── saved_model.pkl
├── scaler.pkl
├── templates/
│ └── index.html

bash
Copy code

## 💻 How to Run
```bash
python train_model.py   # Train model
python app.py           # Start Flask server
