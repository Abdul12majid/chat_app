# Generated by Django 5.1 on 2024-09-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat_app", "0002_friend_profile_friends"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="about",
            field=models.TextField(default="i am using chat app"),
        ),
    ]
