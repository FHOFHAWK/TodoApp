from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users-list', views.UserViewSet)
router.register('users-and-boards', views.UserAndBoardViewSet)

urlpatterns = router.urls

