from django.db import models

# Create your models here.


class User(models.Model):
    USER_CLASS = (
        ('Сторонний', 'Сторонний'),
        ('Сотрудник', 'Сотрудник'),
        ('Администратор', 'Администратор'),
    )

    name = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    login = models.CharField(max_length=40, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    user_class = models.CharField(max_length=15, choices=USER_CLASS, verbose_name="Категория пользователя")

    def __str__(self):
        if self.name:
            return self.name.surname+" ("+self.login+")"
        else:
            return self.login


class Department(models.Model):
    name = models.TextField(max_length=150, verbose_name="Наименование отдела/подзразделения")
    short_name = models.CharField(max_length=50, verbose_name="Сокращенное название", null=True, blank=True)
    adress = models.ForeignKey('AdressDepartment', on_delete=models.SET_NULL, verbose_name="Местонахождение", null=True, blank=True)

    def __str__(self):
        return self.name


class AdressDepartment(models.Model):
    street = models.CharField(max_length=30, verbose_name="Улица")
    building = models.CharField(max_length=10, verbose_name="Дом/Строение")
    letter = models.CharField(max_length=20, verbose_name="Корпус/Литера", null=True, blank=True)
    room = models.CharField(max_length=20, verbose_name="Помещение", null=True, blank=True)

    def __str__(self):
        if not self.letter:
            self.letter = " "
        if not self.room:
            self.room = " "
        return self.street + " " + self.building + self.letter + self.room


class Employee(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', null=True, blank=True)
    position = models.TextField(max_length=50, verbose_name='Должность')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, verbose_name='Отдел/подзразделение', null=True, blank=True)
    phone_work = models.CharField(max_length=15, verbose_name='Рабочий телефон', null=True, blank=True)
    phone_mob = models.CharField(max_length=30, verbose_name='Мобильный телефон', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    office = models.CharField(max_length=10, verbose_name='№ кабинета', null=True, blank=True)
    dob = models.CharField(max_length=20, verbose_name='Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.surname+" "+self.name