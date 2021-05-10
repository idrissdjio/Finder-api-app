from django.db import models

class Item_Category(models.Model):
    """set categories of items to allow founder to easily relocate"""
    category = models.CharField(max_length=255)

    class Meta:
        """override the plural name"""
        verbose_name = 'Item_Category'
        verbose_name_plural = 'Item_Categories'

    def __str__(self):
        return self.category


class Item_City(models.Model):
    """set list of cities where the item can be found"""
    city = models.CharField(max_length=255)

    class Meta:
        """override the plural of city"""
        verbose_name = 'Item_City'
        verbose_name_plural = 'Item_Cities'

    def __str__(self):
        return self.city
