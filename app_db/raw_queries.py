from django.db import connection

def insert_student(name, age, email):
    query = "INSERT INTO app_db_student (name, age, email) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        cursor.execute(query, [name, age, email])

def update_employee_salary(age, new_name):
    query = "UPDATE app_db_student SET name = %s WHERE age = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [new_name, age])

def delete_student(emp_code):
    query = "DELETE FROM app_db_student WHERE age = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [emp_code])
