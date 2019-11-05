from django.contrib import admin

# Register your models here.
from myapp.models import Employee
from myapp.models import Student

admin.site.register(Student)    # Student is registered
admin.site.register(Employee)   # Employee is registered