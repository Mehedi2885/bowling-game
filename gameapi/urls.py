
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FrameViewSet

router = DefaultRouter()

router.register('score', FrameViewSet, basename='score')

"""Url for gameapi app"""
urlpatterns = [
    path('', include(router.urls))
]
