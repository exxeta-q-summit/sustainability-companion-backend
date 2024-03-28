from enum import Enum


class Vehicle(Enum):

    def __init__(
            self,
            vehicle_name,
            co2_emission_in_g_per_km,
            default_occupancy,
            # max_occupancy,
            # default_consumption_in_L_per_100km,
    ):
        self.vehicle_name = vehicle_name
        self.default_occupancy = default_occupancy
        self.co2_emission_in_g_per_km = co2_emission_in_g_per_km
        # self.max_occupancy = max_occupancy
        # self.default_consumption_in_L_per_100km = default_consumption_in_L_per_100km

        ########################
        # An idea could be to add a fuel / resource consumption per (100)km and then calculate the co2 emission based
        # on the fuel type. If a given fuel consumption is provided, the co2 emission is calculated based on the given
        # fuel consumption, like this:
        #                                                         THIS v
        # CAR_BENZIN =    ("CAR_BENZIN",      1,      9,      165,    7.7)
        # if none then use the default consumption
        # if consumption is provided, use the provided consumption: 165 * ( x / 6.2 ) = Y g perkm * km = co2
        #
        # Yo ucould also calculate the co2 emission based on emissions per fuel type:
        # 0.528 g of co2 per g of fuel, comes from papers of the Deutsche Bahn
        # >>> https://co2kompass.bahn.de/Grundlagenbericht_CO2Kompass_1.0.pdf
        #
        # durchschnittlicher Verbrauch von PKW
        # https://de.statista.com/statistik/daten/studie/484054/umfrage/durchschnittsverbrauch-pkw-in-privaten-haushalten-in-deutschland/
        #
        # so you would calculate the co2 emission based on the fuel consumption like this:
        # 0.528 g co2 pro g kraftstoff => 528g co2 per 1 L => for 7.7 L: 528 * 7.7 = 4065g per 100km => per km: 4065/100 ===>>> 40.65g per km/
        ########################

    WALK =          ("WALK",            0,      1)
    BIKE =          ("BIKE",            0,      1)
    BIKE_ELECTRIC = ("BIKE_ELECTRIC",   3,      1)
    CAR_DIESEL =    ("CAR_DIESEL",      173,    1)
    CAR_BENZIN =    ("CAR_BENZIN",      165,    1)
    CAR_ELECTRIC =  ("CAR_ELECTRIC",    79,     1)
    BUS =           ("BUS",             96,     1)
    TRAIN_SHORT =   ("TRAIN_SHORT",     58,     1)
    TRAIN_LONG =    ("TRAIN_LONG",      31,     1)
    AIRPLANE =      ("AIRPLANE",        238,    1)

    def __str__(self):
        return self.vehicle_name
