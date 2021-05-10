from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('postfound', views.FoundViewSet, basename='postfound')

urlpatterns = [
    path('', include(router.urls))
]
