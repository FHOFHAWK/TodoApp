from rest_framework import viewsets
from .models import User, UserAndBoard
from .serializers import UserSerializer, UserAndBoardSerializer
from django.http import HttpResponse


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAndBoardViewSet(viewsets.ModelViewSet):
    serializer_class = UserAndBoardSerializer
    queryset = UserAndBoard.objects.all()
