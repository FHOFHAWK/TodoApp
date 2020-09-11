from django.urls import path
from rest_framework import routers

from .views import AllTasksViewSetWithCheckPostData, MyBoardsView, RetrieveTasksInMyBoardView, RetrieveTaskInMyTasks, \
    AllUsersViewSet, \
    AllBoardsViewSet, AllBoardsAndUsersViewSet, AllColumnsViewSet, AllBoardsAndColumnsViewSet

urlpatterns = [
    path('tasks/', AllTasksViewSetWithCheckPostData.as_view(), name='tasks'),
    path('my-boards/', MyBoardsView.as_view(), name='my-boards'),
    path('my-boards/<int:pk>', RetrieveTasksInMyBoardView.as_view(), name='my-boards-pk'),
    path('my-boards/<int:pk>/<int:tk>', RetrieveTaskInMyTasks.as_view()),
]

router = routers.DefaultRouter()
router.register('users', AllUsersViewSet, basename='all_users')
router.register('boards', AllBoardsViewSet, basename='all_boards')
router.register('users-boards', AllBoardsAndUsersViewSet, basename='all_users_boards')
router.register('columns', AllColumnsViewSet, basename='all_columns')
router.register('boards-columns', AllBoardsAndColumnsViewSet, basename='all_boards_columns')

urlpatterns += router.urls
