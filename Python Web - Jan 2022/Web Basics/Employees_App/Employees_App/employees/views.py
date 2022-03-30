from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Employees_App.employees.models import Department, Employee


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter first name:',
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'},
#         )
#
#     )
#
#     egn = forms.CharField(
#         max_length=10,
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (3, 'DevOps Specialist'),
#         )
#     )


class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model = Employee
        fields = '__all__'


def home(request):
    return HttpResponse("This is home")


def department_details(request):
    return redirect('base')


def index(request):
    context = {
        'description': 'Just a random text to test this',
        'employees': Employee.objects.order_by('first_name', 'last_name').all(),
        'departments': [d.name for d in Department.objects.all()],
        'employee_form': EmployeeForm(),
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


def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            return redirect('index')
    else:
        employee_form = EmployeeForm()

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.all(),
    }
    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit.html', context)