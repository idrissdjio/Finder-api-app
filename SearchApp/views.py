from .serializers import PostSearchSerializer
from .models import PostSearch
from rest_flex_fields.views import FlexFieldsModelViewSet, FlexFieldsMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from .permissions import Search_Item_Permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_flex_fields import is_expanded


class SearchViewSet(FlexFieldsModelViewSet):
    """this modelview allow a user to also expand the data"""

    serializer_class = PostSearchSerializer
    permit_list_expands = ['city_lost', 'category', 'user_profile']
    permission_classes = (Search_Item_Permissions,)
    authentication_classes = (TokenAuthentication, )
    filterset_fields = ('category', 'city_lost', 'name_on_the_item')

    def get_queryset(self):
        queryset = PostSearch.objects.all()

        if is_expanded(self.request, 'city_lost'):
            queryset = queryset.select_related('city_lost')

        if is_expanded(self.request, 'category'):
            queryset = queryset.select_related('category')

        if is_expanded(self.request, 'user_profile'):
            queryset = queryset.select_related('user_profile')

        return queryset
