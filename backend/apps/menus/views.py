from rest_framework import viewsets

from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
