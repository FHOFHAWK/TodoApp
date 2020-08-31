from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated

