from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('boards', views.BoardViewSet)
router.register('tasks', views.TaskViewSet)
router.register('users-and-boards', views.UserAndBoardViewSet)
router.register('users', views.UserViewSet)

urlpatterns = router.urls
