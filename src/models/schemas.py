from pydantic import BaseModel

class StudentSchema(BaseModel):
    name                    : str
    surname                 : str
    father_name             : str
    identification_number   : int
    course_id               : int = 1
    faculty_id              : int = 1
    klass                   : str
    
    class Config:
        orm_mode = True
        
        
class SignIn(BaseModel):
    username    : str
    password    : str
    
    class Config:
        orm_mode = True
            
class SignUp(SignIn):
    access      : bool
    staff_id    : int
    
    class Config:
        orm_mode = True