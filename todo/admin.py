from django.contrib import admin

from .models import Board, BoardsAndUsers, Column, BoardAndColumn, Task

admin.site.register(Board)
admin.site.register(BoardsAndUsers)
admin.site.register(Column)
admin.site.register(BoardAndColumn)
admin.site.register(Task)
