# Generated by Django 3.2.6 on 2021-08-19 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='compid',
        ),
        migrations.DeleteModel(
            name='Empdetails',
        ),
    ]
