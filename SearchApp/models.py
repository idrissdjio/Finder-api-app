from django.db import models
from django.conf import settings
from SelectChoice.models import Item_City, Item_Category

class PostSearch(models.Model):
    """Create a model to allow the user to post a lost item"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    item_picture = models.ImageField(
        max_length=None,
        upload_to='lost_item_pics/',
        default=''
    )
    category = models.ForeignKey(
        Item_Category,
        on_delete=models.CASCADE
    )
    city_lost = models.ForeignKey(
        Item_City,
        on_delete=models.CASCADE
    )
    name_on_the_item = models.CharField(max_length=255)
    description_of_item = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    date_lost = models.DateTimeField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_on_the_item
