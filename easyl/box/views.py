from django.shortcuts import render
from django.contrib.auth.models import User
from box.serializers import UserSerializer
from rest_framework import permissions, viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]




