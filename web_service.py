from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import json
from typing import List
from pydantic import BaseModel, conlist

app = FastAPI()

mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

MODEL_URI = "models:/tracking-quickstart/latest"
model = mlflow.pyfunc.load_model(MODEL_URI)

iris_feature_names = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]

class PredictRequest(BaseModel):
    data: List[List[float]]

class PredictRequest(BaseModel):
    data: List[List[float]]

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}

@app.post("/predict")
async def predict(request: PredictRequest):
    for entry in request.data:
        if len(entry) != 4:
            raise HTTPException(
                status_code=400,
                detail=f"Each data entry must have exactly 4 features. Found entry with {len(entry)} items."
            )
    try:
        df = pd.DataFrame(request.data, columns=iris_feature_names)
        predictions = model.predict(df)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/update-model")
async def update_model(version: int):
    try:
        global model
        new_model_uri = f"models:/tracking-quickstart/{version}"
        model = mlflow.pyfunc.load_model(new_model_uri)
        return {"status": "Model updated successfully", "new_version": version}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

