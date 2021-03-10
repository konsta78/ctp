from django.contrib import admin
from catalog.models import Department, Employee, AdressDepartment, SubdivisionDepartament


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'short_name', 'adress')
    list_filter = ('adress',)

admin.site.register(Department, DepartmentAdmin)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position', 'department', 'email')
    list_filter = ('department', )


@admin.register(AdressDepartment)
class AddressDepartmentAdmin(admin.ModelAdmin):
    list_display = ('street', 'building', 'letter', 'room', 'id')


@admin.register(SubdivisionDepartament)
class SubdivisionDepartamentAdmin(admin.ModelAdmin):
    pass
