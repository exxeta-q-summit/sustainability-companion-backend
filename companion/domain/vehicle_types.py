from django.utils.translation import gettext_lazy as _
from django.db import models


class VehicleTypes(models.TextChoices):
    WALK = "WALK", _("Walking")
    BIKE = "BIKE", _("Cycling")
    BIKE_ELECTRIC = "BIKE_ELECTRIC", _("E-Bike")
    CAR_DIESEL = "CAR_DIESEL", _("Car Diesel")
    CAR_BENZIN = "CAR_BENZIN", _("Car Petrol")
    CAR_ELECTRIC = "CAR_ELECTRIC", _("Car Electric")
    TRAIN_SHORT = "TRAIN_SHORT", _("Train regional")
    TRAIN_LONG = "TRAIN_LONG", _("Train international")
    AIRPLANE = "AIRPLANE", _("Airplane")
    MIXED = "MIXED", _("Mixed")
