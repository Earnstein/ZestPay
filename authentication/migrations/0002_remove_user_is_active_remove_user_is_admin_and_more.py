# Generated by Django 5.0.1 on 2024-01-15 00:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_admin",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_superadmin",
        ),
    ]
