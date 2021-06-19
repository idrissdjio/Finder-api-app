from rest_flex_fields import FlexFieldsModelSerializer
from SelectChoice.models import Item_City, Item_Category
from .models import PostSearch
from Account import AccountSerializers
from rest_framework import serializers


# class Lost_Item_City_Serializer(FlexFieldsModelSerializer):
#     """serialize the lost_city model"""
#     class Meta:
#         model = Item_City
#         fields = ['city']
#
# class Lost_Item_Category_Serializer(FlexFieldsModelSerializer):
#     """serialize the lost_category model"""
#     class Meta:
#         model = Item_Category
#         fields = ['category']

# class PostSearchSerializer(serializers.ModelSerializer):
#     """serialize all the given data by he user"""
#
#     class Meta:
#         model = PostSearch
#         fields = ['id', 'item_picture', 'name_on_the_item', 'description_of_item',
#             'contact', 'date_lost', 'create_on', 'user_profile',
#             'category_item', 'city_item']
#         order_by = ['-created']


class PostSearchSerializer(FlexFieldsModelSerializer):
    """serialize all the given data by he user"""
    item_picture = serializers.ImageField(use_url=True)
    class Meta:
        model = PostSearch
        fields = ['id', 'item_picture', 'name_on_the_item', 'description_of_item',
            'contact', 'date_lost', 'create_on', 'user_profile', 'category_item', 'city_item']
        order_by = ['-created']

        expandable_fields = {
            'user_profile': (AccountSerializers.UserSerializers)
        }
