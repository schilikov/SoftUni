from django.urls import path

from Employees_App.employees.views import department_details, list_departments

urlpatterns = (
    path('list/', list_departments, name='list departments'),
    path('<int:id>/', department_details, name='department details'),
)