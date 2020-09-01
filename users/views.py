from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User, UserAndBoard
from .serializers import UserSerializer, UserAndBoardSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserAndBoardViewSet(viewsets.ModelViewSet):
    serializer_class = UserAndBoardSerializer
    queryset = UserAndBoard.objects.all()
    permission_classes = [IsAuthenticated]
