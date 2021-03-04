from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import Employee, AdressDepartment, Department
from django.contrib.auth.models import User, Group
from openpyxl import load_workbook


class IndexView(View):
    """
    Отображение стартовой страницы
    """

    def get(self, request):
        # добавление пользователя с именем 'test' в группу "testgroup"
        # group = Group.objects.get(name="testgroup")
        # group.user_set.add(User.objects.get(username="test"))

        # num_visits = request.session.get('num_visits', 0)
        # request.session['num_visits'] = num_visits + 1

        employees = Employee.objects.all()
        departments = Department.objects.all()

        context = {"employees": employees, "departments": departments}

        return render(request, 'catalog/index.html', context)


class GovernanceView(View):
    def get(self, request):
        employees = Employee.objects.all()
        departments = Department.objects.filter(name='Руководство')
        context = {"employees": employees, "departments": departments}
        return render(request, 'catalog/index.html', context)


class DepartmentsView(View):
    def get(self, request):
        departments = Department.objects.all().order_by('name')
        context = {"departments": departments}
        return render(request, 'catalog/departments.html', context)


class ResultsView(View):
    def check_find(self, request):
        employees = Employee.objects.all()
        departments = Department.objects.all()
        search = request.GET.get('search')

        if search == "":
            context = {"employees": employees, "departments": departments}
            template = 'catalog/index.html'
        else:
            objects_employess = []
            objects_departments = []

            for employee in employees:
                if (search.lower() in employee.surname.lower() or
                search.lower() in employee.name.lower() or
                search.lower() in employee.patronymic.lower()):

                    objects_employess.append(employee)

            for department in departments:
                if search.lower() in department.name.lower():
                    if department.name.lower().startswith(search.lower()):
                        tmp_str = department.name.lower().replace(search.lower(),
                            "<span style='background-color: yellow'>" + search.capitalize() + "</span>")
                    else:
                        tmp_str = department.name.lower().replace(search.lower(),
                            "<span style='background-color: yellow'>" + search.lower() + "</span>").capitalize()

                    # objects_departments.append(tmp_str) # для подстветки, но не передается весь объект - department
                    objects_departments.append(department)

            context = {"employees": objects_employess, "departments": objects_departments,
                       "count_emp": len(objects_employess), "count_dep": len(objects_departments)}
            template = 'catalog/results.html'

        return context, template

    def get(self, request):
        context, template = self.check_find(request)
        return render(request, template, context)


class EmployeeDetail(generic.DetailView):
    model = Employee


class DepartmentDetail(generic.DetailView):
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class LoadDataBaseView(View):
    def get(self, request):
        if request.user.is_superuser:

            AdressDepartment.objects.update_or_create(
                id=1,
                street='Загородный пр.',
                building='д. 52а',
                letter='Литер А',
                room='пом. 1Н'
            )

            start_cell = 4
            file = 'test.xlsx'
            wb = load_workbook(file)
            sheet = wb.active
            vertical_merged = []
            departments_cells = []

            for cell in range(start_cell, sheet.max_row + 1):
                value = sheet[f'A{cell}'].value
                if value is not None:
                    vertical_merged.append(cell)

            vertical_merged.append(sheet.max_row)

            for i in range(1, len(vertical_merged)):
                departments_cells.append([vertical_merged[i - 1], vertical_merged[i] - vertical_merged[i - 1]])

            for index in range(len(departments_cells)):
                Department.objects.update_or_create(
                    id=index + 1,
                    name=sheet[f'A{departments_cells[index][0]}'].value,
                    adress=AdressDepartment.objects.get(id=1),
                    priority=index
                )

                for i in range(departments_cells[index][1]):
                    current_cell = departments_cells[index][0] + i
                    print(current_cell, sheet[f'B{current_cell}'].value)

                    if sheet[f'C{current_cell}'].value is None:
                        print('merge!')
                    elif sheet[f'D{current_cell}'].value is None:
                        print('Empty!')
                    else:
                        fio = str(sheet[f'D{current_cell}'].value).split()
                        if len(fio) < 3:
                            fio.append(' ')
                        Employee.objects.update_or_create(
                                        surname=fio[0],
                                        name=fio[1],
                                        patronymic=fio[2],
                                        position=sheet[f'C{current_cell}'].value,
                                        department=Department.objects.get(id=index+1),
                                        phone_work=sheet[f'E{current_cell}'].value,
                                        phone_mob=sheet[f'G{current_cell}'].value,
                                        email=sheet[f'H{current_cell}'].value,
                                        office=sheet[f'I{current_cell}'].value,
                                        dob=None
                        )

            employees = Employee.objects.all()
            departments = Department.objects.all()
            context = {"employees": employees, "departments": departments}
            return render(request, 'catalog/index.html', context)


class DeleteDataBaseView(View):
    def get(self, request):
        if request.user.is_superuser:
            Employee.objects.all().delete()
            Department.objects.all().delete()
            AdressDepartment.objects.all().delete()
            return render(request, 'catalog/index.html')