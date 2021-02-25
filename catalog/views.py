from django.shortcuts import render
from django.views import View
from .models import Employee, AdressDepartment, Department
from django.contrib.auth.models import User, Group

# Create your views here.


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

