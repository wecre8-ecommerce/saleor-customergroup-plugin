# Generated by Django 3.2.10 on 2021-12-21 12:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer_group", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customergroup",
            name="customers",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
