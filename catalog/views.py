from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import Employee, AdressDepartment, Department
from django.contrib.auth.models import User, Group


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
