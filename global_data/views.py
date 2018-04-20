# global_data/views.py

from django.shortcuts import render
from django.http import Http404

from .models import Employee, Person


def index(request):
    latest_employees = Employee.objects.order_by('person_id')[:5]
    context = {
        'latest_employees' : latest_employees,
    }
    return render(request, 'global_data/index.html', context)


def employee_detail(request, employee_id):
    """ get the employee details """

    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404("The employee doesn't exist")
    return render(request, 'global_data/detail.html', {'employee': employee})
