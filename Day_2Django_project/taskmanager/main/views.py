from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_all_tasks(request):
    tasks = task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response({"message": "Task deleted successfully"})
