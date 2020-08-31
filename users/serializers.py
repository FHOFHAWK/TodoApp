from rest_framework import serializers
from .models import UserAndBoard, User


class UserAndBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndBoard
        fields = ('user_and_board_id', 'user_name', 'board_title')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_password', 'user_role')
