# Importing Libraries
import pandas as pd
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Annotated,Literal
import joblib
from pathlib import Path

base = Path(__file__).resolve().parent.parent

# App instance
app= FastAPI()

# Loading Model
model = joblib.load(base / "artifacts" / "model.pkl")

# Loading Encoder
encoder = joblib.load(base / "artifacts" / "Encoder.pkl")

# Loading Scaler
scaler = joblib.load(base / "artifacts" / "scaler.pkl")

# Pydantic Object
class Traffic(BaseModel):
    free_flow_speed_kmh : Annotated[float,Field(ge=0,description='Enter Free Flow Speed Kmh')]
    weekend : Annotated[Literal[0,1],Field(...,description='If weekend = 1 and weekdays = 0')]
    time_period : Annotated[Literal['late night','morning','afternoon','evening','night'],
                    Field(...,description='Enter Time Period',
                          examples=['late night','morning','afternoon','evening','night'])]
    travel_time_category : Annotated[Literal['heavy','moderate','fast'],
                            Field(...,description='Enter travel time category',
                                  examples=['heavy','moderate','fast'])]
    speed_kmh : Annotated[float,Field(ge=0,description='Enter Speed in KM/H',examples=[38.3,26.1])]
    rush_hours : Annotated[Literal[0,1],Field(...,description='Enter 1 if rush_hour else 0')]
    hour : Annotated[int,Field(ge=0,le=23,description='Enter hour')]
    travel_time_per_10_km_min : Annotated[float,Field(...,description='Enter Travel Time 10/min')]

# Landing interface
@app.get('/')
def home():
    return {'Text':'Prediction for Congestion Level'}

# Prediction
@app.post("/predict")
def predict(data : Traffic):
    try:
        info = pd.DataFrame([data.model_dump()])
        o_cols = info.select_dtypes(include=['object','category']).columns.to_list()
        n_cols = info.select_dtypes(include=['int','float']).columns.to_list()
        info[o_cols] = encoder.transform(info[o_cols])
        info[n_cols] = scaler.transform(info[n_cols])
        prediction = model.predict(info)[0]
        return JSONResponse(status_code=200,content={'congestion_level':float(prediction)})
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Prediction failed:{str(e)}')