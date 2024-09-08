# Generated by Django 5.1 on 2024-09-08 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat_app", "0003_profile_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatMessage",
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
                ("body", models.TextField()),
                ("seen", models.BooleanField(default=False)),
                (
                    "msg_receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="msg_receiver",
                        to="chat_app.profile",
                    ),
                ),
                (
                    "msg_sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="msg_sender",
                        to="chat_app.profile",
                    ),
                ),
            ],
        ),
    ]
