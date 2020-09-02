from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('boards-list', views.BoardViewSet)
router.register('tasks-list', views.TaskViewSet)
router.register('users-and-boards-list', views.UserAndBoardViewSet)
router.register('users-list', views.UserViewSet)

urlpatterns = router.urls
