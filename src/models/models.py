from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
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
    students_courses        = relationship("Courses", back_populates="courses_students")
    students_faculties      = relationship("Faculties", back_populates="faculties_students")
    
    
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
    id             = Column(Integer, primary_key=True, index=True)
    username       = Column(String, nullable=False)
    password       = Column(String, nullable=False)
    access         = Column(Boolean, nullable=False, default=True)
    staff_id       = Column(Integer, nullable=False, default=1)
    token          = Column(String, nullable=False)
    created_at     = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at     = Column(DateTime, default=datetime.now(), nullable=False)