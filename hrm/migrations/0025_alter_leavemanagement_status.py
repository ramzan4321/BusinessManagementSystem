# Generated by Django 4.1.3 on 2022-11-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0024_alter_leavemanagement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemanagement',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Approved'), ('R', 'Rejected'), ('P', 'Pending')], default='P', max_length=25, null=True),
        ),
    ]
