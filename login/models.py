from django.db import models
from catalog.models import Employee

# Create your models here.


class User(models.Model):
    USER_CLASS = (
        ('Сторонний', 'Сторонний'),
        ('Сотрудник', 'Сотрудник'),
        ('Администратор', 'Администратор'),
    )

    name = models.ForeignKey('catalog.Employee', on_delete=models.CASCADE, null=True, blank=True)
    login = models.CharField(max_length=40, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    user_class = models.CharField(max_length=15, choices=USER_CLASS, verbose_name="Категория пользователя")

    def __str__(self):
        if self.name:
            return self.name.surname+" ("+self.login+")"
        else:
            return self.login