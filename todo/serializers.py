from rest_framework import serializers
from .models import User, UserAndBoard
from .models import Board, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_role')


class UserAndBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndBoard
        fields = ('user_name', 'board_title')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_creation_date', 'board_title')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('board_title', 'task_description', 'task_creation_date', 'task_status', 'task_deadline')
