from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    number_of_registered_ships = models.IntegerField()
    imo_of_ships = models.TextField()
    product_plan = models.CharField(max_length=10, choices=[('freemium', 'Freemium'), ('paid', 'Paid')])

class Ship(models.Model):
    imo_number = models.IntegerField()
    unique_app_identifier = models.CharField(max_length=100)
    vessel_draft = models.FloatField()
    vessel_power_speed_coefficient = models.FloatField()
    type_of_ship = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Captain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    assigned_ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, blank=True, null=True)

class Voyage(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    route_segments = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    historical_conditions = models.TextField()
