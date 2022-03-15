from django.http import HttpResponse
from django.shortcuts import render, redirect

from Employees_App.employees.models import Department, Employee


def home(request):
    return HttpResponse("This is home")


def department_details(request):
    return redirect('base')


def index(request):
    context = {
        'description': 'Just a random text to test this',
        'employees': Employee.objects.order_by('first_name', 'last_name').all(),
        'departments': [d.name for d in Department.objects.all()],
    }
    return render(request, 'index.html', context)


def base(request):
    return render(request, 'base.html')


def list_departments(request):
    context = {
        'employees': Employee.objects.all(),
        'departments': Department.objects.all(),
    }
    return render(request, 'list_departments.html', context)