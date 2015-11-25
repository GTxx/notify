from rest_framework import serializers
from .models import PickUp

class PickUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = PickUp