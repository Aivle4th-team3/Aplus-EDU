# Generated by Django 5.0 on 2024-05-08 06:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="bot_message_embedded",
        ),
        migrations.RemoveField(
            model_name="message",
            name="user_message_embedded",
        ),
    ]
