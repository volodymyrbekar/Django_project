from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
from backend.core.permissions import IsAdmin


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdmin]
