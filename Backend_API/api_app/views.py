from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import MyUser

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = MyUser.objects.all()
    
    serializer_class = UserSerializer
