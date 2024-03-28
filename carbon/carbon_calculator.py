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

        occupancy = max(occupancy, vehicle.default_occupancy)

        co2_emission = vehicle.co2_emission_in_g_per_km * distance_in_km / occupancy

        return co2_emission
