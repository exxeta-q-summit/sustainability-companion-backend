import uuid

from django.db import models

from companion.domain.profile import Profile
from companion.domain.vehicle_types import VehicleTypes


class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,       # ASK YOURSELF IF YOU WANT TO CASCADE DELETE.
        default=None,                   # IT WILL DELETE ALL TRIPS OF A PROFILE WHEN THE PROFILE IS DELETED
        null=True
    )
    start = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    vehicle_type = models.CharField(
        max_length=50,
        choices=VehicleTypes.choices,
        default=VehicleTypes.TRAIN_SHORT
    )
    co2_emissions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True
    )

    def __str__(self):
        return f'{self.profile}: [{self.vehicle_type}] {self.start} -> {self.destination} ({self.co2_emissions}g CO2)'
