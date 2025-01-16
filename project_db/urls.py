from django.contrib import admin
from django.urls import path
from django.urls import path
from app_db import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-student/', views.add_student, name='add_student'),
    #path('update-salary/', views.update_salary, name='update_salary'),
    path('remove-student/', views.remove_student, name='remove_employee'),
    path('update-student/', views.update_detail, name='update_detail'),
]