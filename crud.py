from database import get_connection

def create_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", 
                   (student.name, student.email))
    conn.commit()
    return cursor.lastrowid

def enroll_student(enrollment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)", 
                   (enrollment.student_id, enrollment.course_id))
    conn.commit()
    return cursor.lastrowid

def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()