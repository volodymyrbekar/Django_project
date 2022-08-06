from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Mata:
        model = File
        fields = '__all__'
