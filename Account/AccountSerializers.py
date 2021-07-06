from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from Account import models


class UserSerializers(FlexFieldsModelSerializer):
    """serialize the user model"""
    class Meta:
        fields = ['id', 'phone', 'name', 'location', 'profile_picture', 'password']
        model = models.UserProfile
        extra_kwargs = {
        'password': {
            'write_only': True,
            'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """override the create_user"""
        user = models.UserProfile.objects.create_user(
            phone=validated_data['phone'],
            name=validated_data['name'],
            location=validated_data['location'],
            profile_picture=validated_data['profile_picture'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """"update user profile without changing the password"""

        instance.phone = validated_data['phone']
        instance.name = validated_data['name']
        instance.location = validated_data['location']
        instance.profile_picture = validated_data['profile_picture']
        instance.set_password(validated_data['password'])

        instance.save()

        return instance


# class UserSerializers(serializers.ModelSerializer):
#     """serialize the user model"""
#     class Meta:
#         fields = ['id', 'phone', 'name', 'location', 'profile_picture', 'password']
#         model = models.UserProfile
#         extra_kwargs = {
#         'password': {
#             'write_only': True,
#             'style': {'input_type': 'password'}
#             }
#         }
#
#     def create(self, validated_data):
#         """override the create_user"""
#         user = models.UserProfile.objects.create_user(
#             phone=validated_data['phone'],
#             name=validated_data['name'],
#             location=validated_data['location'],
#             profile_picture=validated_data['profile_picture'],
#             password=validated_data['password'],
#         )
#
#         return user
