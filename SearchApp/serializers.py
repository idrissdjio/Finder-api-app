from rest_flex_fields import FlexFieldsModelSerializer
from .models import Lost_Item_City, Lost_Item_Category, PostSearch
from Account import AccountSerializers


class Lost_Item_City_Serializer(FlexFieldsModelSerializer):
    """serialize the lost_city model"""
    class Meta:
        model = Lost_Item_City
        fields = ['city']

class Lost_Item_Category_Serializer(FlexFieldsModelSerializer):
    """serialize the lost_category model"""
    class Meta:
        model = Lost_Item_Category
        fields = ['category']

class PostSearchSerializer(FlexFieldsModelSerializer):
    """serialize all the given data by he user"""
    class Meta:
        model = PostSearch
        fields = ['id', 'item_picture', 'name_on_the_item', 'description_of_item',
            'contact', 'date_lost', 'create_on', 'user_profile', 'city_lost',
            'category']

        expandable_fields = {
            'category': (Lost_Item_Category_Serializer),
            'city_lost': (Lost_Item_City_Serializer),
            'user_profile': (AccountSerializers.UserSerializers)
        }
