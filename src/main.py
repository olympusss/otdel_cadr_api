from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    course_router,
    faculty_router,
    student_router,
    authentication_router,
    parent_router,
    student_detail_router,
    worked_place_router,
    detail_router
)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(engine)

app.include_router(authentication_router    , tags=["Authentication"])
app.include_router(student_router           , tags=["Students"])
app.include_router(course_router            , tags=["Courses"])
app.include_router(faculty_router           , tags=["Faculties"])
app.include_router(parent_router            , tags=["Parents"])
app.include_router(student_detail_router    , tags=["Student Details"])
app.include_router(worked_place_router      , tags=["Worked Places"])
app.include_router(detail_router            , tags=["Details"])