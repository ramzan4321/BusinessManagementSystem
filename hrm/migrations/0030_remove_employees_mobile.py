# Generated by Django 4.1.3 on 2022-11-23 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0029_alter_employees_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='mobile',
        ),
    ]
