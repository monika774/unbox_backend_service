from rest_framework import serializers
from .models import SpeedData

class SpeedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedData
        fields = ['id', 'speed', 'timestamp']
