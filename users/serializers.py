from rest_framework import serializers
from .models import User, UserAndBoard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_role')


class UserAndBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndBoard
        fields = ('user_name', 'board_title')
