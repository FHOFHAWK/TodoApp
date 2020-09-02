from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User, UserAndBoard
from .serializers import UserSerializer, UserAndBoardSerializer
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserAndBoardViewSet(viewsets.ModelViewSet):
    serializer_class = UserAndBoardSerializer
    queryset = UserAndBoard.objects.all()
    permission_classes = [IsAuthenticated]


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
