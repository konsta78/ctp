# Generated by Django 3.1.6 on 2021-02-13 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.adressdepartment', verbose_name='Местонахождение'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]