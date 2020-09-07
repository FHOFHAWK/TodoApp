from rest_framework import serializers

from .models import User, Board, BoardsAndUsers, Column, BoardAndColumn, Task


class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser')


class AllBoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class AllBoardsAndUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardsAndUsers
        fields = '__all__'


class AllColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'


class AllBoardsAndColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardAndColumn
        fields = '__all__'


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user_name', 'board_title', 'column_title', 'task_description', 'deadline_date')


class RetrieveTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_description', 'column_title', 'deadline_date',)


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_description', 'column_title')
