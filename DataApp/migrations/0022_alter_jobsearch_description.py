# Generated by Django 5.0.4 on 2024-05-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DataApp", "0021_jobsearch_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobsearch",
            name="description",
            field=models.TextField(max_length=300),
        ),
    ]
