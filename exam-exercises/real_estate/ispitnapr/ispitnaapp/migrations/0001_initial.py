# Generated by Django 5.1.6 on 2025-05-24 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agent",
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
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                ("link_to_linkedin", models.URLField()),
                ("number_sales", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Characteristic",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RealEstate",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("area", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_published", models.DateField()),
                ("image", models.ImageField(upload_to="real_estate_images/")),
                ("is_reserved", models.BooleanField()),
                ("is_sold", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="AgentRealEstate",
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
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ispitnaapp.agent",
                    ),
                ),
                (
                    "real_estate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ispitnaapp.realestate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RealEstateCharacteristic",
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
                (
                    "characteristic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ispitnaapp.characteristic",
                    ),
                ),
                (
                    "real_estate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ispitnaapp.realestate",
                    ),
                ),
            ],
        ),
    ]
