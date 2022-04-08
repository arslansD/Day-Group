from django.urls import include, re_path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# Привязываем наше API используя автоматическую маршрутизацию.
# Также мы подключим возможность авторизоваться в браузерной версии API.

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]