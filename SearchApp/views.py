from .serializers import PostSearchSerializer
from .models import PostSearch
from rest_flex_fields.views import FlexFieldsModelViewSet, FlexFieldsMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ViewSet
from .permissions import Search_Item_Permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_flex_fields import is_expanded
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class SearchViewSet(FlexFieldsModelViewSet):
    """this modelview allow a user to also expand the data"""

    parser_classes = (MultiPartParser, )
    serializer_class = PostSearchSerializer
    queryset = PostSearch.objects.all()
    permit_list_expands = ('user_profile',)
    permission_classes = (Search_Item_Permissions,)
    authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name_on_the_item', 'category_item', 'city_item')


    def get_queryset(self):
        queryset = PostSearch.objects.all()

        if is_expanded(self.request, 'user_profile'):
            queryset = queryset.select_related('user_profile')

        return queryset
