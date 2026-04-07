from fastapi import FastAPI ,Path
import json
# read the data from the json file 
def load_data():
    with open('patient.json' , 'r') as f:
        data = json.load(f)
    return data 

app =FastAPI()
@app.get('/person')
def hello():
    return({'message':'somethings is printing'})

@app.get('/about')
def hello():
    return({'message':"this is goddd"})
@app.get('/view')
def view():
    data = load_data() 
    return data

@app.get('/patient/{patient_id}') 
def patient(patient_id: str =Path(...,description="id of patield" ,example="xyz")):
    data = load_data() 
    if patient_id in data:
        return data[patient_id]
    return {'error':"person is not here"}