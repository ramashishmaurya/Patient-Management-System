from pydantic import BaseModel , EmailStr , AnyUrl , Field  ,field_validator
from typing import List ,Dict ,Optional , ClassVar , Annotated
class Patient(BaseModel):
    name: str =Field(max_length=50)
    age: int =Field()
    weight :int  = Field(gt=0)
    linkedin_url:ClassVar[AnyUrl]
    Email:EmailStr
    allergies:Optional[List[str]]=None  # this field is option u can fill or not 
    phone_num :Dict[str ,str]

    @field_validator('Email')
    @classmethod
    def email_validator(cls , values):
        valid_domain = ['hdfc.com' , 'icici.com']
        #ashish@gmail.com
        domain_name = values.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        else:
            print("this is valid person")


 #  this is data 
patient_info = {"name":"ashish", "age":30 , "weight":40,'linkedin_url':'https://www.linkedin.com/in/ashishmaurya09/' ,"Email":"Ashish123@hdfc.com" ,"phone_num":{"email":"Ashishishere@gmail.com" ,"phoneno":"9769295699"}} 
patient1 = Patient(**patient_info) 

#function to print the data inside the basemodel

def patient_detail(patient:Patient):
    print(patient.name)
    print(patient.age) 
    print(patient.allergies)
    print(patient.phone_num)
    print("databases created successfully")

patient_detail(patient1)

