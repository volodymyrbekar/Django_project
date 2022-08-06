from django.contrib import admin
from django import forms

from .models import Restaurant, RestaurantImage


class RestaurantAdmin(admin.ModelAdmin):
    pass


class RestaurantImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantImage, RestaurantImageAdmin)
