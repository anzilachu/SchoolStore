# Generated by Django 4.2.4 on 2023-08-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schoolapp", "0003_rename_cource_student_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="purpose",
            field=models.CharField(
                choices=[
                    ("enquiry", "For Enquiry"),
                    ("order", "Place Order"),
                    ("return", "Return"),
                ],
                max_length=255,
            ),
        ),
    ]
