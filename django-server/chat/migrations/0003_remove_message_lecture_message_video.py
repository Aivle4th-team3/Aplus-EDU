# Generated by Django 5.0 on 2024-01-03 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_message_bot_time_message_user_time"),
        ("lecture", "__first__"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="lecture",
        ),
        migrations.AddField(
            model_name="message",
            name="video",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="lecture.video",
            ),
        ),
    ]