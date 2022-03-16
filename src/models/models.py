from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, Date
from db import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Students(Base):
    __tablename__           = "students"
    id                      = Column(Integer, primary_key=True, index=True)
    name                    = Column(String)
    surname                 = Column(String)
    father_name             = Column(String)
    identification_number   = Column(Integer)
    course_id               = Column(Integer, ForeignKey("courses.id"))
    faculty_id              = Column(Integer, ForeignKey("faculties.id"))
    klass                   = Column(String)
    createAt                = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt                = Column(DateTime, default=datetime.now(), nullable=False)
    students_courses        = relationship("Courses"        , back_populates="courses_students")
    students_faculties      = relationship("Faculties"      , back_populates="faculties_students")
    students_parents        = relationship("Parents"        , back_populates="parents_students")
    students_studentdetail  = relationship("StudentDetail"  , back_populates="studentdetail_students")
    students_workedplaces   = relationship("WorkedPlaces"   , back_populates="workedplaces_students")
    students_detail         = relationship("Detail"         , back_populates="detail_students")
    students_thirddetail    = relationship("ThirdDetail"    , back_populates="thirddetail_students")
    students_images         = relationship("Images"         , back_populates="images_students")
    
    
    
    
class Courses(Base):
    __tablename__           = "courses"
    id                      = Column(Integer, primary_key=True, index=True)
    name                    = Column(String)
    createAt                = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt                = Column(DateTime, default=datetime.now(), nullable=False)
    courses_students        = relationship("Students", back_populates="students_courses")
    
    
class Faculties(Base):
    __tablename__           = "faculties"
    id                      = Column(Integer, primary_key=True, index=True)
    name                    = Column(String)
    dean_id                 = Column(Integer)
    createAt                = Column(DateTime, default=datetime.now(), nullable=False)
    updateAt                = Column(DateTime, default=datetime.now(), nullable=False)
    faculties_students      = relationship("Students", back_populates="students_faculties")
    
    
class Registration(Base):
    __tablename__  = "registration"
    id             = Column(Integer , primary_key=True, index=True)
    username       = Column(String  , nullable=False)
    password       = Column(String  , nullable=False)
    access         = Column(Boolean , nullable=False, default=True)
    staff_id       = Column(Integer , nullable=False, default=1)
    token          = Column(String  , nullable=False)
    created_at     = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at     = Column(DateTime, default=datetime.now(), nullable=False)
    
    
class ParentStatus(Base):
    __tablename__           = "parent_status"
    id                      = Column(Integer , primary_key=True, index=True)
    name                    = Column(String, nullable=False)
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    parentstatus_parents    = relationship("Parents", back_populates="parents_parentstatus")


class Parents(Base):
    __tablename__           = "parents"
    id                      = Column(Integer , primary_key=True, index=True)
    name                    = Column(String, nullable=False)
    surname                 = Column(String, nullable=False)
    father_name             = Column(String, nullable=False)
    birth_place             = Column(String, nullable=False)
    date_of_birth           = Column(Date, nullable=False)
    living_place            = Column(String, nullable=False)
    working_place           = Column(String, nullable=False)
    criminal_record         = Column(String, nullable=False)
    student_id              = Column(Integer, ForeignKey("students.id"))
    parent_status_id        = Column(Integer, ForeignKey("parent_status.id"))
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    parents_parentstatus    = relationship("ParentStatus", back_populates="parentstatus_parents")
    parents_students        = relationship("Students"    , back_populates="students_parents")
    
    
class Region(Base):
    __tablename__           = "region"
    id                      = Column(Integer , primary_key=True, index=True)
    name                    = Column(String, nullable=False)
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    region_studentdetail    = relationship("StudentDetail"     , back_populates="studentdetail_region")
    
    
    
class StudentDetail(Base):
    __tablename__           = "student_detail"
    id                      = Column(Integer , primary_key=True, index=True)
    living_place            = Column(String, nullable=False)
    address                 = Column(String, nullable=False)
    date_of_birth           = Column(Date, nullable=False)
    place_of_birth          = Column(String, nullable=False)
    nationality             = Column(String, nullable=False)
    graduate_school         = Column(String, nullable=False)
    languages               = Column(String, nullable=False)
    speciality              = Column(String, nullable=False)
    academic_degree         = Column(String, nullable=False)
    education               = Column(String, nullable=False)
    party_member            = Column(String, nullable=False)
    other_countries         = Column(String, nullable=False)
    assembled_member        = Column(String, nullable=False)
    student_id              = Column(Integer, ForeignKey("students.id"))
    region_id               = Column(Integer, ForeignKey("region.id"))
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    studentdetail_students  = relationship("Students"   , back_populates="students_studentdetail")
    studentdetail_region    = relationship("Region"     , back_populates="region_studentdetail")
    
    
class WorkedPlaces(Base):
    __tablename__           = "worked_places"
    id                      = Column(Integer , primary_key=True, index=True)
    time                    = Column(String, nullable=False)     
    place                   = Column(String, nullable=False)     
    student_id              = Column(Integer, ForeignKey("students.id"))     
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    workedplaces_students   = relationship("Students", back_populates="students_workedplaces")
    
    
class Detail(Base):
    __tablename__           = "detail"
    id                      = Column(Integer , primary_key=True, index=True)
    address                 = Column(String, nullable=False)
    punish                  = Column(String, nullable=False)
    gender                  = Column(Integer, nullable=False)
    military_service        = Column(Integer, nullable=False)
    in_dormitory            = Column(Boolean, nullable=False)
    room_dormitory          = Column(String, nullable=False)
    passport_number         = Column(String, nullable=False)
    passport_given_date     = Column(Date, nullable=False)
    passport_given_by_whom  = Column(String, nullable=False)
    marital_status          = Column(Integer, nullable=False)
    last_surname            = Column(String, nullable=False)
    leave_dormitory         = Column(Integer, nullable=False)
    speciality              = Column(String, nullable=False)
    student_id              = Column(Integer, ForeignKey("students.id"))
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    detail_students         = relationship("Students", back_populates="students_detail")
    
    
class ThirdDetail(Base):
    __tablename__           = "third_detail"
    id                      = Column(Integer , primary_key=True, index=True)
    home_address            = Column(String, nullable=False)
    home_phone              = Column(String, nullable=False)
    phone_number            = Column(String, nullable=False)
    father_phone_number     = Column(String, nullable=False)
    mother_phone_number     = Column(String, nullable=False)
    student_id              = Column(Integer, ForeignKey("students.id"))
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    thirddetail_students    = relationship("Students", back_populates="students_thirddetail")
    
    
class Images(Base):
    __tablename__           = "images"
    id                      = Column(Integer , primary_key=True, index=True)
    img                     = Column(String, nullable=False)
    student_id              = Column(Integer, ForeignKey("students.id"))
    created_at              = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at              = Column(DateTime, default=datetime.now(), nullable=False)
    images_students         = relationship("Students", back_populates="students_images")