from datetime import datetime
from django.db import models

# Create your models here.


class Task(models.Model):
    class Status(models.TextChoices):
        TO_DO = "TO DO", "To do"
        IN_PROGRESS = "IN PROGRESS", "In progress"
        COMPLETED = "COMPLETED", "Completed"

    id = models.AutoField(primary_key=True, editable=False)
    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.TO_DO, db_index=True
    )
    date_created = models.DateTimeField(default=datetime.now())
    date_updated = models.DateTimeField(default=datetime.now())
