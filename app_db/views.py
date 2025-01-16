from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .raw_queries import insert_student, delete_student, update_employee_salary, update_detail

def add_employee(request):
    # Example data
    
    name = 'Jonna'
    age = 25
    email = 'jonna.wick@gmail.com'

    insert_student(name, age, email)
    return JsonResponse({'message': 'Employee added successfully'})


def update_detail(request):
    age = 45
    new_name = 'Wick'

    update_student_name(age, new_name)
    return JsonResponse({'Message' : 'Student name updated successfully'})

def update_salary(request):
    # Example data
    age = 45
    new_name = 'John Satham'

    update_employee_salary(age, new_name)
    return JsonResponse({'message': 'Employee salary updated successfully'})

def remove_student(request):
    # Example data
    age = 25

    delete_student(age)
    return JsonResponse({'message': 'Employee deleted successfully'})
