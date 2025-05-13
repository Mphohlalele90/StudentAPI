from fastapi import FastAPI
from models import Student, Enrollment
import crud

app = FastAPI()

@app.post("/students/")
def create_student(student: Student):
    student_id = crud.create_student(student)
    return {"id": student_id, "message": "Student added"}

@app.post("/enroll/")
def enroll(enrollment: Enrollment):
    enrollment_id = crud.enroll_student(enrollment)
    return {"id": enrollment_id, "message": "Student enrolled"}

@app.get("/students/")
def read_students():
    return crud.get_students()