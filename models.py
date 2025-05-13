from pydantic import BaseModel

class Student(BaseModel):
    name: str
    email: str

class Course(BaseModel):
    name: str
    description: str

class Enrollment(BaseModel):
    student_id: int
    course_id: int

    