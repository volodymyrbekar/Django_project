from django.db import models

from backend.core.models import BaseModel, BaseImage
from ckeditor.fields import RichTextField


class Restaurant(BaseModel):
    title = models.CharField(max_length=256, blank=True)
    body = RichTextField()

    def __str__(self):
        return self


class RestaurantImage(BaseImage):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
