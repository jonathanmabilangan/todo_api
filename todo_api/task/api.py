from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .services import create_task, update_task, remove_task
from task.selectors import task_list
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "task_name",
            "task_description",
            "status",
            "order",
        )


class TaskNewAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        task_name = serializers.CharField()
        task_description = serializers.CharField(required=False, default="")

    @extend_schema(
        request=InputSerializer,
        responses={201: TaskSerializer},
    )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        if serializer.is_valid():
            task = create_task(user=request.user, **serializer.validated_data)
            data = TaskSerializer(task).data
            return Response(data, status=status.HTTP_201_CREATED)


class TaskUpdateAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        task_name = serializers.CharField(required=False)
        task_description = serializers.CharField(required=False)
        status = serializers.CharField(required=False)
        order = serializers.IntegerField(min_value=0)

    @extend_schema(
        request=InputSerializer,
        responses={200: TaskSerializer},
    )
    def put(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        if serializer.is_valid():
            task = update_task(pk=pk, user=request.user, **serializer.validated_data)
            data = TaskSerializer(task).data
            return Response(data, status=status.HTTP_200_OK)


class TaskRemoveAPIView(APIView):
    def delete(self, request, pk):
        remove_task(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListAPIView(APIView):
    @extend_schema(responses={200: TaskSerializer(many=True)})
    def get(self, request):
        task = task_list()
        data = TaskSerializer(task, many=True).data
        return Response(data)
