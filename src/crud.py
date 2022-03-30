from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, asc, desc, true
from models import \
    (
        Students, Courses, Faculties, StudentSchema, SignIn, SignUp, Registration,
        ParentStatus, Parents, ParentSchema, Region, StudentDetail, StudentDetailSchema,
        WorkedPlaceSchema, WorkedPlaces, Detail, DetailSchema, ThirdDetail, ThirdDetailSchema,
        Images, FilterSchema
    )
from token_handler import create_access_token
from upload_dependence import upload_image, delete_uploaded_image
import json
from datetime import datetime

async def read_courses(db: Session):
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
    
    
async def read_faculties(db: Session):
    result = db.query(
        Faculties.id,
        Faculties.name
    ).all()
    if result:
        return result
    f = open("json/fakultetler.json")
    data = json.load(f)
    for i in data:
        name_json = i.get("name")
        new_add = Faculties(
            name = name_json
        )
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return None
    f.close()
    result = db.query(
        Faculties.id,
        Faculties.name
    ).all()
    if result:
        return result
    else:
        return None
    

async def create_student(db: Session, student: StudentSchema):
    new_add = Students(**student.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return new_add.id
    else:
        return None
    
    
async def read_students(db: Session, page, limit):
    result = db.query(
        Students.id,
        Students.name,
        Students.surname,
        Students.father_name,
        Students.identification_number,
        Students.klass,
        Students.course_id,
        Students.faculty_id,
        # StudentDetail.living_place,
        # StudentDetail.address,
        # StudentDetail.date_of_birth,
        # StudentDetail.place_of_birth,
        # StudentDetail.nationality,
        # StudentDetail.graduate_school,
        # StudentDetail.languages,
        # StudentDetail.speciality,
        # StudentDetail.academic_degree,
        # StudentDetail.education,
        # StudentDetail.party_member,
        # StudentDetail.other_countries,
        # StudentDetail.assembled_member,
        # StudentDetail.region_id,
        # Detail.address,               
        # Detail.punish,                
        # Detail.gender,                
        # Detail.military_service,
        # Detail.in_dormitory,
        # Detail.room_dormitory,
        # Detail.passport_number,
        # Detail.passport_given_date,
        # Detail.passport_given_by_whom,
        # Detail.marital_status,
        # Detail.last_surname,
        # Detail.leave_dormitory,
        # Detail.speciality,
        # ThirdDetail.home_address,
        # ThirdDetail.home_phone,
        # ThirdDetail.phone_number,
        # ThirdDetail.father_phone_number,
        # ThirdDetail.mother_phone_number
    )
    # result = result.join(StudentDetail, StudentDetail.student_id == Students.id)
    # result = result.join(Detail, Detail.student_id == Students.id)
    # result = result.join(ThirdDetail, ThirdDetail.student_id == Students.id)
    # * Filter faculty
    # if filter.facultuies is not None:
        # result = result.filter(or_(Students.faculty_id == elem for elem in filter.facultuies))
    
    # # * Filter speciality
    # if filter.speciality is not None:
    #     result = result.filter(or_(Detail.speciality == elem for elem in filter.speciality))
    
    # # * Filter class
    # if filter.klass is not None:
    #     result = result.filter(or_(Students.klass == elem for elem in filter.klass))
    
    # # * Filter gender
    # if filter.gender is not None:
    #     if filter.gender == 1:
    #         result = result.filter(Detail.gender == 1)
    #     elif filter.gender == 2:
    #         result = result.filter(Detail.gender == 2)
    
    # # * Filter in_dormitory
    # if filter.in_dormitory is not None:
    #     if filter.in_dormitory == 0:
    #         result = result.filter(Detail.in_dormitory == 0)
    #     elif filter.in_dormitory == 1:
    #         result = result.filter(Detail.in_dormitory == 1)
    
    # # * Filter date of birth
    # if filter.date_of_birth is not None:
    #     result = result.filter(or_(StudentDetail.date_of_birth.year == elem for elem in filter.date_of_birth))
        
    # # * Filter regions
    # if filter.regions is not None:
    #     result = result.filter(or_(StudentDetail.region_id == elem for elem in filter.regions))
        
    # # * Filter nationality
    # if filter.nationality is not None:
    #     result = result.filter(or_(StudentDetail.nationality == elem for elem in filter.nationality))
        
    # # * Filter leave dormitory
    # if filter.leave_dormitory is not None:
    #     if filter.leave_dormitory == 0:
    #         result = result.filter(Detail.leave_dormitory == 0)
    #     elif filter.leave_dormitory == 1:
    #         result = result.filter(Detail.leave_dormitory == 1)
    
    # # * Filter military service
    # if filter.military_service is not None:
    #     if filter.military_service == 0:
    #         result = result.filter(Detail.military_service == 0)
    #     if filter.military_service == 1:
    #         result = result.filter(Detail.military_service == 1)
            
    # # * Filter course
    # if filter.course is not None:
    #     result = result.filter(or_(Students.course_id == elem for elem in filter.course))
        
    # # * Filter marital status
    # if filter.marital_status is not None:
    #     if filter.marital_status == 0:
    #         result = result.filter(Detail.marital_status == 0)
    #     elif filter.marital_status == 1:
    #         result = result.filter(Detail.marital_status == 1)
    
    result_count = result.count()
    result = result.order_by(desc(Students.id)).offset(limit * (page - 1)).limit(limit).all()
    if result:
        new_list = []
        for res in result:
            res = dict(res)
            res["img"] = await read_uploaded_images(db=db, student_id=res["id"])
            new_list.append(res)
        result = new_list
    final = {}
    final["students"]   = result
    final["page_count"] = (result_count // limit) + 1
    if final:
        return final
    else:
        return None
    
    
async def read_current_student(db: Session, id):
    result = db.query(
        Students.id,
        Students.name,
        Students.surname,
        Students.father_name,
        Students.identification_number,
        Students.klass,
        Students.course_id,
        Students.faculty_id,
    #     StudentDetail.living_place,
    #     StudentDetail.address,
    #     StudentDetail.date_of_birth,
    #     StudentDetail.place_of_birth,
    #     StudentDetail.nationality,
    #     StudentDetail.graduate_school,
    #     StudentDetail.languages,
    #     StudentDetail.speciality,
    #     StudentDetail.academic_degree,
    #     StudentDetail.education,
    #     StudentDetail.party_member,
    #     StudentDetail.other_countries,
    #     StudentDetail.assembled_member,
    #     StudentDetail.region_id,
    #     Detail.address,               
    #     Detail.punish,                
    #     Detail.gender,                
    #     Detail.military_service,
    #     Detail.in_dormitory,
    #     Detail.room_dormitory,
    #     Detail.passport_number,
    #     Detail.passport_given_date,
    #     Detail.passport_given_by_whom,
    #     Detail.marital_status,
    #     Detail.last_surname,
    #     Detail.leave_dormitory,
    #     Detail.speciality,
    #     ThirdDetail.home_address,
    #     ThirdDetail.home_phone,
    #     ThirdDetail.phone_number,
    #     ThirdDetail.father_phone_number,
    #     ThirdDetail.mother_phone_number
    # )
    # result = result.join(StudentDetail, StudentDetail.student_id == Students.id)
    # result = result.join(Detail, Detail.student_id == Students.id)
    # result = result.join(ThirdDetail, ThirdDetail.student_id == Students.id)
    )
    result = result.filter(Students.id == id).first()
    if result:
        result = dict(result)
        result["img"] = await read_uploaded_images(db=db, student_id=id)
    if result:
        return result
    else:
        return None
   
    
async def read_uploaded_images(db: Session, student_id):
    result = db.query(Images.img.label("img_name"))\
    .filter(Images.student_id == student_id)\
    .first()
    if result:
        return result[0][1:]
    else:
        return None


async def update_student(db: Session, id, student: StudentSchema):
    new_update = db.query(Students)\
    .filter(Students.id == id)\
    .update({
        Students.name                   : student.name,
        Students.surname                : student.surname,
        Students.father_name            : student.father_name,
        Students.identification_number  : student.identification_number,
        Students.course_id              : student.course_id,
        Students.faculty_id             : student.faculty_id,
        Students.klass                  : student.klass
    }, synchronize_session=False)
    db.commit()
    if new_update:
        return True
    else:
        return None
    
    
async def delete_student(db: Session, id):
    new_delete = db.query(Students)\
    .filter(Students.id == id)\
    .delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return True
    else:
        None
        
        
async def create_sign_up(db: Session, req: SignUp):
    get_user = db.query(
        Registration.username,
        Registration.password
    )\
    .filter(
        and_(
            Registration.username == req.username,
            Registration.password == req.password
        )
    )\
    .first()
    if get_user:
        return None
    token_dict = {
        "username" : req.username,
        "password" : req.password
    }
    token = create_access_token(data=token_dict)
    new_add = Registration(
        **req.dict(),
        token = token
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return token
    else:
        return None
    
    
async def read_sign_in(db: Session, req: SignIn):
    result = db.query(
        Registration.token
    )\
    .filter(
        and_(
            Registration.username == req.username,
            Registration.password == req.password
        )
    ).first()
    if result:
        return result
    else:
        return None
    
    
async def read_parent_status(db: Session):
    result = db.query(
        ParentStatus.id,
        ParentStatus.name
    ).all()
    if result:
        return result
    
    f = open("json/parent_status.json")
    data = json.load(f)
    for i in data:
        name_json = i.get("name")
        new_add = ParentStatus(
            name = name_json
        )
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return None
    f.close()
    result = db.query(
        ParentStatus.id,
        ParentStatus.name
    ).all()
    if result:
        return result
    else:
        return None


async def read_current_parents(db: Session, student_id):
    result = db.query(
        Parents.id,
        Parents.name,
        Parents.surname,
        Parents.father_name,
        Parents.birth_place,
        Parents.date_of_birth,
        Parents.living_place,
        Parents.working_place,
        Parents.criminal_record,
        Parents.student_id,
        Parents.parent_status_id
    )\
    .filter(Parents.student_id == student_id)\
    .all()
    if result:
        return result
    else:
        return None
    
    
async def create_parent(db: Session, parent: ParentSchema):
    str2date = datetime.strptime(parent.date_of_birth, '%d/%m/%Y').date()
    new_add = Parents(
        name                = parent.name,
        surname             = parent.surname,
        father_name         = parent.father_name,
        birth_place         = parent.birth_place,
        date_of_birth       = str2date,
        living_place        = parent.living_place,
        working_place       = parent.working_place,
        criminal_record     = parent.criminal_record,
        student_id          = parent.student_id,
        parent_status_id    = parent.parent_status_id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return new_add.id
    else:
        return None
    
    
async def delete_parent(db: Session, id):
    new_delete = db.query(Parents)\
    .filter(Parents.id == id)\
    .delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return True
    else:
        return None
    
    
async def read_region(db: Session):
    result = db.query(
        Region.id,
        Region.name
    ).all()
    if result:
        return result
    
    f = open("json/welayatlar.json")
    data = json.load(f)
    for i in data:
        name_json = i.get("name")
        new_add = Region(
            name = name_json
        )
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        if not new_add:
            return None
    f.close()
    result = db.query(
        Region.id,
        Region.name
    ).all()
    if result:
        return result
    else:
        return None
    
    
async def read_student_detail(db: Session, student_id):
    result = db.query(
        StudentDetail.id,
        StudentDetail.living_place,
        StudentDetail.address,
        StudentDetail.date_of_birth,
        StudentDetail.place_of_birth,
        StudentDetail.nationality,
        StudentDetail.graduate_school,
        StudentDetail.languages,
        StudentDetail.speciality,
        StudentDetail.academic_degree,
        StudentDetail.education,
        StudentDetail.party_member,
        StudentDetail.other_countries,
        StudentDetail.assembled_member,
        StudentDetail.student_id,
        StudentDetail.region_id,
        StudentDetail.created_at,
        StudentDetail.updated_at
    )\
    .filter(StudentDetail.student_id == student_id)\
    .all()
    if result:
        return result
    else:
        return None
    
    
async def create_student_detail(db: Session, req: StudentDetailSchema):
    new_add = StudentDetail(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return new_add.id
    else:
        return None
    
    
async def update_student_detail(db: Session, req: StudentDetailSchema, id):
    new_update = db.query(StudentDetail)\
    .filter(StudentDetail.id == id)\
    .update({
        StudentDetail.living_place      : req.living_place,
        StudentDetail.address           : req.address,
        StudentDetail.date_of_birth     : req.date_of_birth,
        StudentDetail.place_of_birth    : req.place_of_birth,
        StudentDetail.nationality       : req.nationality,
        StudentDetail.graduate_school   : req.graduate_school,
        StudentDetail.languages         : req.languages,
        StudentDetail.speciality        : req.speciality,
        StudentDetail.academic_degree   : req.academic_degree,
        StudentDetail.education         : req.education,
        StudentDetail.party_member      : req.party_member,
        StudentDetail.other_countries   : req.other_countries,
        StudentDetail.assembled_member  : req.assembled_member,
        StudentDetail.student_id        : req.student_id,
        StudentDetail.region_id         : req.region_id
    }, synchronize_session=False)
    db.commit()
    if new_update:
        return True
    else:
        return False
    
    
async def create_worked_place(db: Session, req: WorkedPlaceSchema):
    new_add = WorkedPlaces(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return new_add.id
    else:
        return None
    
    
async def read_worked_places(db: Session, student_id):
    result = db.query(
        WorkedPlaces.id,
        WorkedPlaces.time,
        WorkedPlaces.place,
        WorkedPlaces.student_id
    )\
    .filter(WorkedPlaces.student_id == student_id)\
    .all()
    if result:
        return result
    else:
        return None
    
    
async def update_worked_place(db: Session, id, req: WorkedPlaceSchema):
    new_update = db.query(WorkedPlaces)\
    .filter(WorkedPlaces.id == id)\
    .update({
        WorkedPlaces.time           : req.time,
        WorkedPlaces.place          : req.place,
        WorkedPlaces.student_id     : req.student_id
    }, synchronize_session=False)
    db.commit()
    if new_update:
        return True
    else:
        return None
    
async def read_detail(db: Session, student_id):
    result = db.query(
        Detail.id,                      
        Detail.address,                 
        Detail.punish,                  
        Detail.gender,                  
        Detail.military_service,        
        Detail.in_dormitory,            
        Detail.room_dormitory,          
        Detail.passport_number,         
        Detail.passport_given_date,     
        Detail.passport_given_by_whom,  
        Detail.marital_status,          
        Detail.last_surname,            
        Detail.leave_dormitory,         
        Detail.speciality,              
        Detail.student_id              
    )\
    .filter(Detail.student_id == student_id)\
    .all()
    if result:
        return result
    else:
        return None
    
    
async def create_detail(db: Session, req: DetailSchema):
    new_add = Detail(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return new_add.id
    else:
        return None
    
    
async def update_detail(db: Session, id, req: DetailSchema):
    new_update = db.query(Detail)\
    .filter(Detail.id == id)\
    .update({
        Detail.address                  : req.address,                 
        Detail.punish                   : req.punish,                  
        Detail.gender                   : req.gender,                  
        Detail.military_service         : req.military_service,        
        Detail.in_dormitory             : req.in_dormitory,            
        Detail.room_dormitory           : req.room_dormitory,          
        Detail.passport_number          : req.passport_number,         
        Detail.passport_given_date      : req.passport_given_date,     
        Detail.passport_given_by_whom   : req.passport_given_by_whom,  
        Detail.marital_status           : req.marital_status,          
        Detail.last_surname             : req.last_surname,            
        Detail.leave_dormitory          : req.leave_dormitory,         
        Detail.speciality               : req.speciality,              
        Detail.student_id               : req.student_id 
    }, synchronize_session=False)
    db.commit()
    if new_update:
        return True
    else:
        return None
    
    
async def delete_worked_place(db: Session, id):
    new_delete = db.query(WorkedPlaces)\
    .filter(WorkedPlaces.id == id)\
    .delete(synchronize_session=False)
    db.commit()
    if new_delete:
        return True
    else:
        return None
    
    
async def read_third_detail(db: Session, student_id):
    result = db.query(
        ThirdDetail.id,
        ThirdDetail.home_address,
        ThirdDetail.home_phone,
        ThirdDetail.phone_number,
        ThirdDetail.father_phone_number,
        ThirdDetail.mother_phone_number,
        ThirdDetail.student_id
    )\
    .filter(ThirdDetail.student_id == student_id)\
    .all()
    if result:
        return result
    else:
        return None
    
    
async def create_third_detail(db: Session, req: ThirdDetailSchema):
    new_add = ThirdDetail(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return new_add.id
    else:
        return None
    
    
async def update_third_detail(db: Session, id, req: ThirdDetailSchema):
    new_update = db.query(ThirdDetail)\
    .filter(ThirdDetail.id == id)\
    .update({
        ThirdDetail.home_address        : req.home_address,
        ThirdDetail.home_phone          : req.home_phone,
        ThirdDetail.phone_number        : req.phone_number,
        ThirdDetail.father_phone_number : req.father_phone_number,
        ThirdDetail.mother_phone_number : req.mother_phone_number,
        ThirdDetail.student_id          : req.student_id
    }, synchronize_session=False)
    db.commit()
    if new_update:
        return True
    else:
        return None
    
    
async def create_student_image(db: Session, student_id, file):
    get_images = db.query(
        Images.img
    )\
    .filter(Images.student_id == student_id)\
    .all()
    if get_images:
        for images in get_images:
            if images.img is not None:
                delete_uploaded_image(image_name=images.img)
        db.query(Images).filter(Images.student_id == student_id)\
            .delete(synchronize_session=False)
        db.commit()
    uploaded_img_name = upload_image(directory="img", file=file)
    if not uploaded_img_name:
        return None
    new_add = Images(
        img         = uploaded_img_name,
        student_id  = student_id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    if new_add:
        return True
    else:
        return None