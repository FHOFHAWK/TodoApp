from django.contrib import admin
from .models import User, UserAndBoard, Board, Task

admin.site.register(User)
admin.site.register(UserAndBoard)
admin.site.register(Board)
admin.site.register(Task)
