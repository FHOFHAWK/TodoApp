from django.db import models


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_creation_date = models.DateField(auto_now_add=True)
    board_title = models.CharField(max_length=50)


class Task(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='board_id_of_task')
    task_description = models.TextField()
    task_creation_date = models.DateTimeField(auto_now_add=True)
    task_status = models.CharField(max_length=50)
    task_deadline = models.DateField()
