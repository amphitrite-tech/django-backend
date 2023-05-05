from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Organization, Ship, User, Voyage
from .serializers import OrganizationSerializer, ShipSerializer, CaptainSerializer, VoyageSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .permissions import IsCaptainOrAdmin


# User Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CaptainSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CaptainSerializer


# Organization Views
class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


# Ship Views
class ShipListCreateView(generics.ListCreateAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class ShipRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


# Voyage Views
class VoyageListCreateView(generics.ListCreateAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer


class VoyageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user_id': self.user.id})
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ShipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    permission_classes = [IsCaptainOrAdmin]
