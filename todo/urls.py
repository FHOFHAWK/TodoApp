from django.urls import path

from rest_framework import routers

from . import views
from .views import AllTasksViewSet, MyBoardsView, RetrieveTasksInMyBoardView, RetrieveTaskInMyTasks

urlpatterns = [
    path('tasks/', AllTasksViewSet.as_view()),
    path('my-boards/', MyBoardsView.as_view()),
    path('my-boards/<int:pk>', RetrieveTasksInMyBoardView.as_view()),
    path('my-boards/<int:pk>/<int:tk>', RetrieveTaskInMyTasks.as_view()),
]

router = routers.DefaultRouter()
router.register('users', views.AllUsersViewSet, basename='all_users')
router.register('boards', views.AllBoardsViewSet, basename='all_boards')
router.register('users-boards', views.AllBoardsAndUsersViewSet, basename='all_users_boards')
router.register('columns', views.AllColumnsViewSet, basename='all_columns')
router.register('boards-columns', views.AllBoardsAndColumnsViewSet, basename='all_boards_columns')

urlpatterns += router.urls
