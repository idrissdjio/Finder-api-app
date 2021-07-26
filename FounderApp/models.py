# from django.db import models
# from django.conf import settings
# from Account.models import UserProfile
# from SelectChoice.models import Item_City, Item_Category
#
# class PostFound(models.Model):
#     """create a model to allow user to post a found item"""
#     user_profile = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     found_city = models.ForeignKey(
#         Item_City,
#         on_delete=models.CASCADE
#     )
#     category = models.ForeignKey(
#         Item_Category,
#         on_delete=models.CASCADE
#     )
#     item_picture = models.ImageField(
#         max_length=None,
#         upload_to='found_item_pic/',
#         default='',
#     )
#     name_on_item = models.CharField(max_length=255)
#     picking_location = models.CharField(max_length=255)
#     date_found = models.DateTimeField()
#     create_on = models.DateTimeField(auto_now_add=True)
#     contact = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name_on_item

from django.db import models
from django.conf import settings
from SelectChoice.models import Item_City, Item_Category
from django.utils.timezone import now
from cloudinary.models import CloudinaryField

import base64

class PostFound(models.Model):
    """Create a model to allow the user to post a lost item"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # item_picture = models.ImageField(
    #     max_length=None,
    #     upload_to='lost_item_pics/',
    #     default=''
    # )
    item_picture = CloudinaryField('image')
    # category = models.ForeignKey(
    #     Item_Category,
    #     on_delete=models.CASCADE,
    #     default=''
    # )
    # city_lost = models.ForeignKey(
    #     Item_City,
    #     on_delete=models.CASCADE,
    #     default=''
    # )
    name_on_the_item = models.CharField(max_length=255)
    description_of_item = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=255)
    date_lost = models.DateTimeField(default=now)
    create_on = models.DateTimeField(auto_now_add=True)
    picking_location = models.CharField(max_length=255)

    category_item = models.CharField(max_length=255, default='')
    city_item = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['-create_on']


    def __str__(self):
        return self.name_on_the_item
