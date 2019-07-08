from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import CreateUserViewSet

router = routers.DefaultRouter()
router.register('create_user', CreateUserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
