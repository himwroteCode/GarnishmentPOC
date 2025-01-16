
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('update-salary/', views.update_salary, name='update_salary'),
    path('remove-student/', views.remove_employee, name='remove_employee'),
]



