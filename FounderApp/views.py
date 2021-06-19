from .serializers import Found_Serializer
from .models import PostFound
from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from .permissions import Found_Permissions
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class FoundViewSet(FlexFieldsModelViewSet):
    """Set a view for the PostFound"""
    parser_classes = (MultiPartParser, )

    serializer_class = Found_Serializer
    permit_list_expands = ('user_profile', )
    permission_classes = (Found_Permissions, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['city_item', 'category_item', 'name_on_the_item']


    def get_queryset(self):
        queryset = PostFound.objects.all()

        if is_expanded(self.request, 'user_profile'):
            queryset = queryset.select_related('user_profile')


        return queryset
