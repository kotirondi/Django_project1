# Generated by Django 5.0.4 on 2024-08-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Login", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("account_number", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("aadhar_number", models.CharField(max_length=12, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("date_of_creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]