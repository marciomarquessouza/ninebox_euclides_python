# ninebox/global_data/models.py

from django.db import models


class Year (models.Model):
    """ Reference Year for NineBox Modules """

    year = models.CharField(max_length=4)
    description = models.CharField(max_length=4000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.year


class Version (models.Model):
    """ Version fro Ninebox Modules """

    version = models.CharField(max_length=12)
    description = models.CharField(max_length=4000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.version


class Department (models.Model):
    """ Employee Department """

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    company_code_01 = models.CharField(max_length=40)
    company_code_02 = models.CharField(max_length=40)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    version = models.ForeignKey(Version,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Designation (models.Model):
    """ Employee Designation """

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    company_code_01 = models.CharField(max_length=40)
    company_code_02 = models.CharField(max_length=40)
    year = models.ForeignKey(Year, on_delete= models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Person (models.Model):
    """ Person details """

    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    document_code_01 = models.CharField(max_length=255)
    document_code_02 = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee (models.Model):
    """ Employee Details """

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    company_code_01 = models.CharField(max_length=40)
    company_code_02 = models.CharField(max_length=40)
    company_code_03 = models.CharField(max_length=40)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_evaluator = models.BooleanField(default=False)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    picture = models.CharField(max_length=4000)

    def __str__(self):
        return self.person.name
