from django.contrib import admin
from catalog.models import Department, Employee, AdressDepartment
from login.models import User

# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(AdressDepartment)
admin.site.register(User)