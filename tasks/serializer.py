from rest_framework import serializers
from .models import Task


class TaskSerialize(serializers.ModelSerializer):  #convert model to json
    class Meta:
        model = Task
        fields = "__all__"
