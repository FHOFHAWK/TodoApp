from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Board, BoardsAndUsers, Column, BoardAndColumn, Task
from .serializers import AllUsersSerializer, AllBoardsSerializer, AllBoardsAndUsersSerializer, AllColumnsSerializer, \
    AllBoardsAndColumnsSerializer, AllTasksSerializer, RetrieveTaskSerializer, UpdateTaskSerializer
from .services import check_input_data_in_db


class AllUsersViewSet(viewsets.ModelViewSet):
    """
    Вывод списка всех пользователей + функционал CRUD
    """
    queryset = User.objects.all()
    serializer_class = AllUsersSerializer
    permission_classes = [IsAdminUser]


class AllBoardsViewSet(viewsets.ModelViewSet):
    """
    Вывод списка всех досок + функционал CRUD
    """
    queryset = Board.objects.all()
    serializer_class = AllBoardsSerializer
    permission_classes = [IsAdminUser]


class AllBoardsAndUsersViewSet(viewsets.ModelViewSet):
    """
    Вывод списка всех досок с пользователями + функционал CRUD
    """
    queryset = BoardsAndUsers.objects.all()
    serializer_class = AllBoardsAndUsersSerializer
    permission_classes = [IsAdminUser]


class AllColumnsViewSet(viewsets.ModelViewSet):
    """
    Вывод списка всех колонок + функционал CRUD
    """
    queryset = Column.objects.all()
    serializer_class = AllColumnsSerializer
    permission_classes = [IsAdminUser]


class AllBoardsAndColumnsViewSet(viewsets.ModelViewSet):
    """
    Вывод списка всех досок с их колонками + функционал CRUD
    """
    queryset = BoardAndColumn.objects.all()
    serializer_class = AllBoardsAndColumnsSerializer
    permission_classes = [IsAdminUser]


class AllTasksViewSetWithCheckPostData(APIView):
    queryset = Task.objects.all()
    serializer_class = AllTasksSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = AllTasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        post_data = self.request.data
        if check_input_data_in_db(post_data) is True:
            new_task = Task.objects.create(
                user_name=User.objects.get(id=post_data["user_name"]),
                board_title=Board.objects.get(id=post_data["board_title"]),
                column_title=Column.objects.get(id=post_data["column_title"]),
                task_description=post_data["task_description"])
            new_task.save()
            serializer = AllTasksSerializer(new_task)
            return Response(serializer.data)
        else:
            return Response('Введены неверные данные')


class MyBoardsView(ListAPIView):
    serializer_class = AllBoardsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()

    def get(self, request, *args, **kwargs):
        user_name = self.request.user
        user = User.objects.filter(username=user_name)
        boards = BoardsAndUsers.objects.filter(user_name=user[0].id)
        serializer = AllBoardsSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveTasksInMyBoardView(ListAPIView):
    serializer_class = RetrieveTaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.filter()

    def get(self, request, *args, **kwargs):
        board = BoardAndColumn.objects.get(id=kwargs['pk'])
        tasks = Task.objects.filter(board_title_id=board.board_title_id)
        serializer = RetrieveTaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveTaskInMyTasks(RetrieveUpdateAPIView):
    serializer_class = RetrieveTaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        get_object_or_404(BoardAndColumn, id=kwargs['pk'])
        task = Task.objects.filter(id=kwargs['tk'])
        serializer = UpdateTaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['tk'])
        new_column = get_object_or_404(Column, id=self.request.data['column_title'])
        task.column_title = new_column
        task.save()
        serializer = UpdateTaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
