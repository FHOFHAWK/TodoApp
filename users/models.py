from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name


class UserAndBoard(models.Model):
    user_and_board_id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    board_title = models.ForeignKey('boards.Board', on_delete=models.CASCADE)

