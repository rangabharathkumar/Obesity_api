from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model_utils import predict_obesity

app = FastAPI()

class InputData(BaseModel):
    Gender: str
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

@app.get("/")
def read_root():
    return {"message": "🏥 Obesity Prediction API is live!"}

@app.post("/predict")
def predict(data: InputData):
    try:
        prediction = predict_obesity(data.dict())
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
