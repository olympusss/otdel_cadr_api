from sqlalchemy.orm import Session
from models import (Students, Courses, Faculties)
import json

def read_courses(db: Session):
    result = db.query(
        Courses.id,
        Courses.name,
    ).all()
    if result:
        return result
    f = open("json/courses.json")
    data = json.load(f)
    for i in data:
        name_json = i.get("name")
        new_add = Courses(
            name = name_json
        )
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return None
    f.close()
    result = db.query(
        Courses.id,
        Courses.name
    ).all()
    if result:
        return result
    else:
        return None