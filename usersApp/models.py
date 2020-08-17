from django.db import models


class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=150, unique=True, )
	password = models.CharField(max_length=150, )
	role = models.CharField(max_length=10, )


class UserAndBoard(models.Model):
	user_and_board_id = models.AutoField(primary_key=True)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	board_title = models.ForeignKey('boardsApp.Board', on_delete=models.CASCADE)
