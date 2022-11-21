# Generated by Django 4.1.3 on 2022-11-16 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0018_alter_leavemanagement_leave_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemanagement',
            name='leave_type',
            field=models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_title',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='hrm.tasktitle'),
        ),
    ]
