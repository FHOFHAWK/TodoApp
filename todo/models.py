from django.db import models


class User(models.Model):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    COMMON_USER = 'common_user'

    USER_ROLES_CHOICES = [
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (COMMON_USER, 'Common user'),
    ]

    user_name = models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя')
    user_password = models.CharField(max_length=50, verbose_name='Пароль пользователя')
    user_role = models.CharField(max_length=15, choices=USER_ROLES_CHOICES, default=COMMON_USER,
                                 verbose_name='Права пользователя')

    def __str__(self):
        return self.user_name


class Board(models.Model):
    board_title = models.CharField(max_length=50, verbose_name='Название доски')
    board_creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания доски')

    def __str__(self):
        return self.board_title


class Task(models.Model):
    board_title = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Задача находится в доске')
    task_description = models.TextField(verbose_name='Описание задачи')
    task_creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')
    task_deadline = models.DateTimeField(verbose_name='Срок выполнения задачи')

    def __str__(self):
        return self.task_description


class UserAndTask(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Номер таска')
