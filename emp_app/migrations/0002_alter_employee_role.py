# Generated by Django 3.2.12 on 2023-09-26 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.role'),
        ),
    ]
