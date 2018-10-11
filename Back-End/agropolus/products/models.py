from core.models import SoftDeletionModel, TaggingMixin
from django.conf import settings
from django.db import models


# Create your models here.

class Category(TaggingMixin, SoftDeletionModel):
    parent_category = models.ForeignKey('self', related_name='child_categories_related', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=settings.CATEGORY_PICTURES_URL, blank=True)


class Product(TaggingMixin, SoftDeletionModel):
    name = models.CharField(max_length=64)
    price = models.BigIntegerField()
    picture = models.ImageField(upload_to=settings.PRODUCT_PICTURES_URL, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
