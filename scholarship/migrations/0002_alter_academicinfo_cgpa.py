# Generated by Django 5.1.2 on 2024-11-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scholarship", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicinfo",
            name="cgpa",
            field=models.CharField(max_length=20),
        ),
    ]
