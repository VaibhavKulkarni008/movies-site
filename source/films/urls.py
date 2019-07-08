from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import MoviesViewSet, DirectorViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register('movies', MoviesViewSet)
router.register('director', DirectorViewSet)
router.register('genre', GenreViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
