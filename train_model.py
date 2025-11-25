# train_model.py

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# Load dataset
df = pd.read_csv("dataset_sdn.csv")  # already uploaded

# Keep ONLY 5 FEATURES
features = ['pktcount', 'bytecount', 'pktrate', 'flows', 'Protocol']
df = df[features + ['label']]

# Encode any string column
encoder = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = encoder.fit_transform(df[col])

# Split X & y
X = df[features]
y = df['label']

# Balance dataset with SMOTE
smote = SMOTE()
X, y = smote.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train best model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model & scaler for Flask
pickle.dump(model, open("saved_model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("🔥 Model trained and saved: saved_model.pkl + scaler.pkl")
