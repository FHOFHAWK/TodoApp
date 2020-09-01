from rest_framework import serializers
from .models import User, UserAndBoard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserAndBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndBoard
        fields = ('user_and_board_id', 'user_name', 'board_title')
