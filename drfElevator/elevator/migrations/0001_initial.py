# Generated by Django 4.2 on 2023-04-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Request",
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
                ("floor_no", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Elevator",
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
                ("current_floor", models.IntegerField(default=0)),
                ("direction", models.CharField(default="N", max_length=10)),
                ("is_door_open", models.BooleanField(default=False)),
                ("is_operational", models.BooleanField(default=True)),
                ("request", models.ManyToManyField(blank=True, to="elevator.request")),
            ],
        ),
    ]