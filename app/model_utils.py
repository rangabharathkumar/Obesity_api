import joblib
import pandas as pd

# Load artifacts
model = joblib.load("app/artifacts/xgb_obesity_model.joblib")
scaler = joblib.load("app/artifacts/scaler .pkl")
label_encoders = joblib.load("app/artifacts/label_encoders .pkl")

expected_features = [
    'Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight',
    'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC',
    'FAF', 'TUE', 'CALC', 'MTRANS'
]

def preprocess_input(data: dict) -> pd.DataFrame:
    df = pd.DataFrame([data])

    # Apply encoders
    for col, le in label_encoders.items():
        if col in df.columns:
            df[col] = le.transform(df[col])

    # Apply scaler
    df[scaler.feature_names_in_] = scaler.transform(df[scaler.feature_names_in_])
    return df

def predict_obesity(data: dict) -> int:
    processed = preprocess_input(data)
    prediction = model.predict(processed)[0]
    return int(prediction)
