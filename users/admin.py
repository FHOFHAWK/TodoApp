from django.contrib import admin
from .models import UserAndBoard, User

admin.site.register(User)
admin.site.register(UserAndBoard)
