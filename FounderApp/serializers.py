from .models import PostFound
from SelectChoice.models import Item_City, Item_Category
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from Account import AccountSerializers

class Item_City_Serializer(FlexFieldsModelSerializer):
    """serialize the city model"""
    class Meta:
        model = Item_City
        fields = ('city',)

class Item_Category_Serializer(FlexFieldsModelSerializer):
    """serialize the category model"""
    class Meta:
        model = Item_Category
        fields = ('category',)

# class Found_Serializer(FlexFieldsModelSerializer):
#     """serialize the postfound model and let the user expand the fields"""
#     class Meta:
#         model = PostFound
#         fields = ('id', 'user_profile', 'found_city', 'category',
#             'item_picture', 'name_on_item', 'picking_location', 'date_found',
#             'create_on', 'contact')
#         expandable_fields = {
#             'found_city': (Item_City_Serializer),
#             'category': (Item_Category_Serializer),
#             'user_profile': (AccountSerializers.UserSerializers)
#         }

class Found_Serializer(FlexFieldsModelSerializer):
    """serialize the postfound model and let the user expand the fields"""
    item_picture = serializers.ImageField(use_url=True)
    class Meta:
        model = PostFound
        fields = ['id', 'item_picture', 'name_on_the_item', 'description_of_item',
            'contact', 'date_lost', 'create_on', 'user_profile', 'category_item', 'city_item', 'picking_location']
        order_by = ['-created']
        expandable_fields = {
            'user_profile': (AccountSerializers.UserSerializers)
        }
