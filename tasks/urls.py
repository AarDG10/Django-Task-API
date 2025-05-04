from rest_framework import routers
from tasks import views
from django.urls import path, include
from django.contrib import admin
from .views import TaskListCreateView, TaskEditDeleteView

# api versioning
#router = routers.DefaultRouter()
#router.register(r"tasks", views.TaskView, "task")

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('<int:pk>/', TaskEditDeleteView.as_view()),
]