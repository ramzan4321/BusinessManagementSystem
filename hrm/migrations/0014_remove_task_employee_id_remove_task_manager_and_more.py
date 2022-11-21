# Generated by Django 4.1.3 on 2022-11-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0013_alter_employeesworkdetails_submit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='submit_date',
        ),
        migrations.AddField(
            model_name='employeesworkdetails',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'Not Assigned'), ('A', 'Assigned'), ('C', 'Completed')], default='N', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='employeesworkdetails',
            name='submit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
