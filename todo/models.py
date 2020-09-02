from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_creation_date = models.DateField(auto_now_add=True)
    board_title = models.CharField(max_length=50)


class UserAndBoard(models.Model):
    user_and_board_id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE)


class Task(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='board_id_of_task')
    task_description = models.TextField()
    task_creation_date = models.DateTimeField(auto_now_add=True)
    task_status = models.CharField(max_length=50)
    task_deadline = models.DateField()
