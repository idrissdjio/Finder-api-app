from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Account import views

router = DefaultRouter()
router.register('register', views.UserViewSet, basename='UserViewSet')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginViewSet.as_view()),
    path('logout/', views.UserLogoutView.as_view())
]
