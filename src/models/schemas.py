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
        

class ParentSchema(BaseModel):
    name                : str
    surname             : str
    father_name         : str
    birth_place         : str
    date_of_birth       : str
    living_place        : str
    working_place       : str
    criminal_record     : str
    student_id          : int
    parent_status_id    : int
    
    class Config:
        orm_mode = True
        
        
class StudentDetailSchema(BaseModel):
    living_place        : str
    address             : str
    date_of_birth       : str
    place_of_birth      : str
    nationality         : str
    graduate_school     : str
    languages           : str
    speciality          : str
    academic_degree     : str
    education           : str
    party_member        : str
    other_countries     : str
    assembled_member    : str
    student_id          : int
    region_id           : int
    
    class Config:
        orm_mode = True
        
        
class WorkedPlaceSchema(BaseModel):
    time                : str
    place               : str
    student_id          : int
    
    class Config:
        orm_mode = True
        

class DetailSchema(BaseModel):
    address                 : str
    punish                  : str
    gender                  : int
    military_service        : int
    in_dormitory            : bool
    room_dormitory          : str
    passport_number         : str
    passport_given_date     : str
    passport_given_by_whom  : str
    marital_status          : int
    last_surname            : str
    leave_dormitory         : int
    speciality              : str
    student_id              : int
    
    class Config:
        orm_mode = True