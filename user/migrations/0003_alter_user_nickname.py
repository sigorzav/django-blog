# Generated by Django 5.1.5 on 2025-01-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
