from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name


class Board(models.Model):
    board_title = models.CharField(max_length=50)
    board_creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.board_title


class UserAndBoard(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE)


class Task(models.Model):
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Задача находится в доске')
    task_description = models.TextField(verbose_name='Описание задачи')
    task_creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')
    task_status = models.CharField(max_length=50, verbose_name='Статус задачи')
    task_deadline = models.DateTimeField(verbose_name='Срок выполнения задачи')

    def __str__(self):
        return self.task_description
