from django.contrib import admin
from .models import User, UserAndTask, Board, Task

admin.site.register(User)
admin.site.register(UserAndTask)
admin.site.register(Board)
admin.site.register(Task)
