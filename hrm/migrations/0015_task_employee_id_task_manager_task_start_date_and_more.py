# Generated by Django 4.1.3 on 2022-11-16 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrm', '0014_remove_task_employee_id_remove_task_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_task', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_task', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'Not Assigned'), ('A', 'Assigned'), ('C', 'Completed')], default='N', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='submit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
