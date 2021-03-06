# Generated by Django 3.2.9 on 2021-12-09 06:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256)),
                ("description", models.TextField(blank=True)),
                ("is_active", models.BooleanField(default=True)),
                ("date", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "customers",
                    models.ManyToManyField(
                        blank=True, null=True, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
