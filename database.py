import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="674692",
        database="student_portal"
    )