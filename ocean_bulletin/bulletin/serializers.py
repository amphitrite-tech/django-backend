from rest_framework import serializers
from .models import Organization, Ship, Captain, Voyage

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'

class CaptainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captain
        fields = '__all__'

class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = '__all__'
