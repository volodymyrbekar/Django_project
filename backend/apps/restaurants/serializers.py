from rest_framework.serializers import ModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Restaurant, RestaurantImage


class RestaurantImageSerializer(ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )


class RestaurantSerializer(ModelSerializer):
    image = RestaurantImageSerializer(source='restaurantimage_set', many=True)

    class Mata:
        model = Restaurant
        fields = '__all__'
