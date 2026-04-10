from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Literal
import json

app = FastAPI()

def load_data():
    try:
        with open('patient.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)
def base():
    return {'message': 'checking the server is on'}

class Patient(BaseModel):
    id: str
    name: str 
    height: int
    weight: int
    gender: Literal['male', 'female']

@app.post('/create')
def createpost(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="patient already exists")
    # that values is coming and has to make 
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)

    return JSONResponse(
        status_code=201,
        content={'message': 'data is created successfully'}
    )

@app.get('/view')
def view():
    data = load_data()
    return data 
