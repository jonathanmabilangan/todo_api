from django.shortcuts import get_object_or_404

from .models import Task

def task_list():
    return Task.objects.all().order_by("status")

def get_task(task_id):
    return get_object_or_404(Task, id=task_id)