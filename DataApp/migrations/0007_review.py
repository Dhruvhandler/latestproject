# Generated by Django 5.0.2 on 2024-03-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DataApp", "0006_userregister"),
    ]

    operations = [
        migrations.CreateModel(
            name="review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("message", models.CharField(max_length=500)),
            ],
        ),
    ]
