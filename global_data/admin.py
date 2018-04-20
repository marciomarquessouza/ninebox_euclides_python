# ninebox/global_data/admin.py

from django.contrib import admin
from .models import Person, Employee, Department, Designation, Version, Year

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Version)
admin.site.register(Year)
