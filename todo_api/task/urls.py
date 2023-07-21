from django.urls import path

from . import api

urlpatterns = [
    path("task/list", api.TaskListAPIView.as_view(), name="list-task"),
    path("task/create/", api.TaskNewAPIView.as_view(), name="new-task"),
    path("task/<int:pk>/update/", api.TaskUpdateAPIView.as_view(), name="update-task"),
    path("task/<int:pk>/remove/", api.TaskRemoveAPIView.as_view(), name="remove-task"),
]
