# Generated by Django 5.0 on 2024-01-08 06:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lecture", "0008_enrollment_playback_duration_alter_enrollment_user_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="enrollment",
            unique_together={("user", "lecture")},
        ),
        migrations.RemoveField(
            model_name="video",
            name="users",
        ),
        migrations.AddField(
            model_name="enrollment",
            name="lecture",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollments",
                to="lecture.lecture",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="lecture",
            name="users",
            field=models.ManyToManyField(
                related_name="lectures",
                through="lecture.Enrollment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="video",
        ),
    ]
