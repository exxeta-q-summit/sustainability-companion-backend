from carbon.vehicle_enum import Vehicle


# calculate carbon footprint based on various parameters

class Calculator:

    @staticmethod
    def simple(distance_in_km: float, vehicle: Vehicle, occupancy: int = None) -> float:
        """
        Calculate CO2 emission based on the given parameters
        :param vehicle: vehicle type
        :param distance_in_km: distance in kilometers
        :param occupancy: number of passengers
        :return: CO2 emission in grams
        """

        if occupancy is None:
            occupancy = vehicle.max_occupancy or 1

        co2_emission = vehicle.co2_emission_per_km * distance_in_km / occupancy

        return co2_emission

    @staticmethod
    def complex(distance: float, consumption_per_km: float, occupancy: int = None) -> float:
        """
        Calculate CO2 emission based on the given parameters
        :param distance: distance in kilometers
        :param consumption_per_km: consumption per kilometer
        :param occupancy: number of passengers
        :return: CO2 emission in grams
        """

        co2_emission = consumption_per_km * distance / occupancy
        return co2_emission
