# Generated by Django 4.2.7 on 2023-11-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdata",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("TEACHER", "Teacher"),
                    ("STUDENT", "Student"),
                ],
                default="STUDENT",
                max_length=10,
            ),
        ),
    ]
