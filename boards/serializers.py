from rest_framework import serializers
from .models import Board, Task


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_id', 'board_creation_date', 'board_title')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('board_id', 'task_description', 'task_creation_date', 'task_status', 'task_deadline')
