# Generated by Django 4.2.4 on 2023-08-18 05:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schoolapp", "0002_student_purpose"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="cource",
            new_name="course",
        ),
    ]
