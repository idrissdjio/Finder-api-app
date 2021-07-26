from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .AccountSerializers import UserSerializers
from .models import UserProfile
from .permissions import UpdateOwnProfile


class UserViewSet(FlexFieldsModelViewSet):
    """User ViewSet for adding and edit user instances"""
    serializer_class = UserSerializers
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(phone=self.request.user.phone)
        return self.queryset


class UserLoginViewSet(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserLogoutView(APIView):
    """enable the user to logout and destroy his token"""
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
