# Generated by Django 4.2.11 on 2024-04-24 19:30

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=128)),
            ],
            options={
                "verbose_name": "User",
                "abstract": False,
            },
        ),
    ]