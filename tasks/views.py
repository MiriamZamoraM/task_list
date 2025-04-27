from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tasks
from .serializers import TaskSerializer, TaskUpSerializer


class TaskCreateView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskViewGet(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        task_list = Tasks.objects.all()
        return Response(task_list, status.HTTP_200_OK)
    


class IDTaskAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, pk):
        task_obj = Tasks.objects.filter(pk=pk, status_delete=False)
        serializer = TaskSerializer(task_obj, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        
        task_obj = get_object_or_404(Tasks, pk=pk, status_delete=False)
        serializer = TaskUpSerializer(instance=task_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        task_obj = get_object_or_404(Tasks, pk=pk, status_delete=False)
        task_obj.status_delete = True
        task_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)