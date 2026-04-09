from pydantic import BaseModel
# create the model right 
class Patient(BaseModel):
    name: str
    age: int
#  this is data 
patient_info = {"name":"ashish", "age":30} 
patient1 = Patient(**patient_info) 
#
def patient_detail(patient:Patient):
    print(patient.name)
    print(patient.age) 
    print("databases created successfully")

patient_detail(patient1)