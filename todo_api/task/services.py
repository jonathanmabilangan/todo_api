from django.db import transaction

from .models import Task
from .selectors import get_task


@transaction.atomic
def create_task(task_name: str, task_description: str) -> Task:
    try:
        task = Task.objects.create(
            task_name=task_name,
            task_description=task_description,
            status=Task.Status.TO_DO,
        )
        return task
    except Exception as exc:
        raise exc


@transaction.atomic
def update_task(pk: int, **kwargs) -> Task:
    task = get_task(task_id=pk)
    for field, value in kwargs.items():
        if field in ["task_name", "task_description", "status"]:
            setattr(task, field, value)
            task.save()
        # else:
        #     return "Failed to save."
    return task


@transaction.atomic
def remove_task(pk: int):
    task = get_task(task_id=pk)
    task.delete()
    return f"Task id: {pk} has been removed"