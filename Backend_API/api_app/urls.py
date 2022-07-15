from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/',include(router.urls))
    
]