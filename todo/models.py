from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    board_title = models.CharField(unique=True, max_length=50, verbose_name='Название доски')

    def __str__(self):
        return self.board_title


class BoardsAndUsers(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Название доски')


class Column(models.Model):
    column_title = models.CharField(max_length=50, verbose_name='Название колонки')

    def __str__(self):
        return self.column_title


class BoardAndColumn(models.Model):
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Название доски')
    column_title = models.ForeignKey(Column, on_delete=models.CASCADE, verbose_name='Название колонки')


class Task(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Название доски')
    column_title = models.ForeignKey(Column, on_delete=models.CASCADE, verbose_name='Название колонки')
    task_description = models.CharField(max_length=50, verbose_name='Описание задачи')
    deadline_date = models.DateTimeField(auto_now_add=True)
