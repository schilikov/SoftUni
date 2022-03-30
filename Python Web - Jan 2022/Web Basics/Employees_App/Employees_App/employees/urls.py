from django.urls import path

from Employees_App.employees.views import department_details, list_departments, create_employee, edit_employee

urlpatterns = (
    path('list/', list_departments, name='list departments'),
    path('<int:id>/', department_details, name='department details'),
    path('create/', create_employee, name='create employee'),
    path('edit/<int:pk>/', edit_employee, name='edit employee'),
)
