from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
import json # when you use json file then it's neccasary to import 

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')

def about():
    return {'message':'${A fully function API to manage your patient records}'}


@app.get('/view')

def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
def patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')
