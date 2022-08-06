from django.db import models

from backend.core.models import BaseModel


class File(BaseModel):
    title = models.CharField(max_length=256, default='Mo title')
    file = models.FileField(upload_to='menus')

    def __str__(self):
        return self.title
