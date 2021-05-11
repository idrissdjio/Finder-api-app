from .serializers import Found_Serializer
from .models import PostFound
from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from .permissions import Found_Permissions
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters


class FoundViewSet(FlexFieldsModelViewSet):
    """Set a view for the PostFound"""
    serializer_class = Found_Serializer
    permit_list_expands = ('user_profile', 'found_city', 'category')
    permission_classes = (Found_Permissions, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['user_profile', 'found_city', 'category', 'name_on_item']


    def get_queryset(self):
        queryset = PostFound.objects.all()

        if is_expanded(self.request, 'user_profile'):
            queryset = queryset.select_related('user_profile')

        if is_expanded(self.request, 'found_city'):
            queryset = queryset.select_related('found_city')

        if is_expanded(self.request, 'category'):
            queryset = queryset.select_related('category')

        return queryset
