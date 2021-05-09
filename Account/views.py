from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings

from .AccountSerializers import UserSerializers
from .models import UserProfile
from .permissions import UpdateOwnProfile

class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet for adding and edit user instances"""
    serializer_class = UserSerializers
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)


class UserLoginViewSet(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
