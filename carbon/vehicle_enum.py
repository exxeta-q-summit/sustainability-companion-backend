from enum import Enum


class Vehicle(Enum):

    def __init__(self, vehicle_name, co2_emission_in_g_per_km, max_occupancy):
        self.vehicle_name = vehicle_name
        self.co2_emission_per_km = co2_emission_in_g_per_km
        self.max_occupancy = max_occupancy

    WALK =          ("WALK",            1,      1)
    BIKE =          ("BIKE",            2,      1)
    BIKE_ELECTRIC = ("BIKE_ELECTRIC",   1,      1)
    CAR_DIESEL =    ("CAR_DIESEL",      1,      9)
    CAR_BENZIN =    ("CAR_BENZIN",      1,      9)
    CAR_ELECTRIC =  ("CAR_ELECTRIC",    0,      9)
    BUS =           ("BUS",             1,      50)
    TRAIN_SHORT =   ("TRAIN_SHORT",     0.5,    None)
    TRAIN_LONG =    ("TRAIN_LONG",      2,      None)
    AIRPLANE =      ("AIRPLANE",        1,      None)
    MIXED =         ("MIXED",           0,      None)

    def __str__(self):
        return self.vehicle_name
