from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Task
from .serializer import TaskSerialize

from django.utils.dateparse import parse_date

class TaskListCreateView(APIView):  #business logic (2 Separate classes, maintaining modularity)
    def get(self, request):  #GET Request endpoint for fetching and filtering data
        queryset = Task.objects.all()
        search = request.GET.get('search')
        search_date = request.GET.get('search_date')
        sort_by_date = request.GET.get('sort_by_date')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if search_date:
            try:
                date_obj = parse_date(search_date)
                queryset = queryset.filter(date=date_obj)
            except:
                return Response({"error": "Invalid date format"}, status=400)

        if sort_by_date == "true":
            queryset = queryset.order_by('date')

        serializer = TaskSerialize(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):  #Post Request endpoint for adding a task into list
        serializer = TaskSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskEditDeleteView(APIView):
    def patch(self, request, pk): #Patch Request endpoint for editing a task from the list
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerialize(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): #Delete Request endpoint for deleting a task from the list
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
