from django.db import models
from django.conf import settings


class Lost_Item_Category(models.Model):
    """List of categories of lost items"""
    category = models.CharField(max_length=255)

    class Meta:
        """here we override the plural name in the db"""
        verbose_name = ('Lost_Item_Category')
        verbose_name_plural = ('Lost_Item_Categories')

    def __str__(self):
        return self.category


class Lost_Item_City(models.Model):
    """List of cities of lost items"""
    city = models.CharField(max_length=255)

    class Meta:
        """override the city name in the db"""
        verbose_name = ('Lost_Item_City')
        verbose_name_plural = ('Lost_Item_Cities')

    def __str__(self):
        return self.city



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
        Lost_Item_Category,
        on_delete=models.CASCADE
    )
    city_lost = models.ForeignKey(
        Lost_Item_City,
        on_delete=models.CASCADE
    )
    name_on_the_item = models.CharField(max_length=255)
    description_of_item = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    date_lost = models.DateTimeField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_on_the_item
