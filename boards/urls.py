from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('boards-list', views.BoardViewSet)
router.register('tasks-list', views.TaskViewSet)

urlpatterns = router.urls

