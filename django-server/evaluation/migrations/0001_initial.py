# Generated by Django 5.0 on 2024-01-08 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("lecture", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestPaper",
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
                ("question", models.TextField(default="")),
                ("answer", models.TextField(default="")),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testpapers",
                        to="lecture.video",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TestResult",
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
                ("evaluation_date", models.DateField(auto_now_add=True)),
                ("scrore", models.IntegerField(default=0)),
                (
                    "testpaper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="evaluation.testpaper",
                    ),
                ),
            ],
        ),
    ]
