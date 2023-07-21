from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response


from task.services import create_task, update_task, remove_task
from task.selectors import task_list
from task.models import Task


class TaskSerializer(serializers.Serializer):
    task_name = serializers.CharField()
    task_description = serializers.CharField()
    status = serializers.CharField()

    class Meta:
        model = Task
        fields = (
            "id",
            "task_name",
            "task_description",
            "status",
        )


class TaskNewAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        # if serializer.is_valid():
        #     task = create_task(**serializer.validated_data)
        #     data = TaskSerializer(task).data
        #     return Response(data, status=status.HTTP_201_CREATED)


class TaskUpdateAPIView(APIView):
    def put(self, request, pk):
        serializer = TaskSerializer(data=request.data)
        # if serializer.is_valid():
        #     task = update_task(pk=pk, **serializer.validated_data)
        #     data = TaskSerializer(task).data
        #     return Response(data, status=status.HTTP_200_OK)


class TaskRemoveAPIView(APIView):
    def delete(self, request, pk):
        remove_task(pk=pk)
        return Response(status=status.HTTP_200_OK)


class TaskListAPIView(APIView):
    # class Pagination(LimitOffsetPagination):
    #     default_limit = 50
    #     max_limit = 100

    # pagination_class = Pagination

    def get(self, request):
        task = task_list()
        data = TaskSerializer(task, many=True).data
        return Response(data)
