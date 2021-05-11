from django.db import models
from django.conf import settings
from Account.models import UserProfile
from SelectChoice.models import Item_City, Item_Category

class PostFound(models.Model):
    """create a model to allow user to post a found item"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    found_city = models.ForeignKey(
        Item_City,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Item_Category,
        on_delete=models.CASCADE
    )
    item_picture = models.ImageField(
        max_length=None,
        upload_to='found_item_pic/',
        default='',
    )
    name_on_item = models.CharField(max_length=255)
    picking_location = models.CharField(max_length=255)
    date_found = models.DateTimeField()
    create_on = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name_on_item
