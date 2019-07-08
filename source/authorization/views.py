from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserSerializer


class CreateUserViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
