from django.utils.translation import gettext_lazy as _
from django.db import models


class VehicleTypes(models.TextChoices):
    CAR_DIESEL = "CAR_DIESEL", _("Car Diesel")
    CAR_PETROL = "CAR_PETROL", _("Car Petrol")
    CAR_ELECTRIC = "CAR_ELECTRIC", _("Car Electric")
    WALKING = "WALKING", _("WALKING")
    BIKE = "BIKE", _("Cycling")
    MIXED = "MIXED", _("MIXED")
    TRAIN_SHORT = "TRAIN_SHORT", _("Train regional")
    TRAIN_LONG = "TRAIN_LONG", _("Train international")
