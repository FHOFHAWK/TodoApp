from rest_framework import serializers
from .models import User, UserAndTask
from .models import Board, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'user_role')


class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_role')


class UserAndTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndTask
        fields = ('user_name', 'task_id')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
