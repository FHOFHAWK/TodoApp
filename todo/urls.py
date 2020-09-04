from . import views
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('check/', views.TestAPIView.as_view()),
]

router = routers.DefaultRouter()
router.register('boards/all', views.BoardViewSet)
router.register('tasks/all', views.AllTasksViewSet, basename='all_tasks')
# router.register('tasks', views.TaskViewSet)
router.register('users-and-boards', views.UserAndTaskViewSet)
router.register('users', views.UserViewSet)

urlpatterns += router.urls
