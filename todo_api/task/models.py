from datetime import datetime
from django.db import models
from django.utils import timezone

from ordered_model.models import OrderedModel

# Create your models here.


class Task(OrderedModel):
    class Status(models.TextChoices):
        TO_DO = "TO DO", "To do"
        IN_PROGRESS = "IN PROGRESS", "In progress"
        COMPLETED = "COMPLETED", "Completed"

    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.TO_DO, db_index=True
    )
    date_created = models.DateTimeField(default=timezone.now())
    date_updated = models.DateTimeField(auto_now=True)

    order_with_respect_to = "user"
