from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Create your views here.
