# Generated by Django 4.1.3 on 2022-11-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0019_alter_leavemanagement_leave_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktitle',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'Not Assigned'), ('A', 'Assigned'), ('C', 'Completed')], default='N', max_length=25, null=True),
        ),
    ]
