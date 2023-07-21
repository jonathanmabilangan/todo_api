# Generated by Django 4.2.3 on 2023-07-21 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("task_name", models.CharField(max_length=255)),
                ("task_description", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("TO DO", "To do"),
                            ("IN PROGRESS", "In progress"),
                            ("COMPLETED", "Completed"),
                        ],
                        db_index=True,
                        default="TO DO",
                        max_length=50,
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023,
                            7,
                            21,
                            19,
                            27,
                            21,
                            266798,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]
