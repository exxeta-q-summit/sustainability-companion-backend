import json

from django.http import JsonResponse, HttpResponse
from rest_framework import status

from carbon.carbon_calculator import Calculator
from carbon.vehicle_enum import Vehicle


class CarbonApi:

    @classmethod
    def basic(cls, request):
        try:
            distance = float(request.GET['km'])
            vehicle_type = request.GET['vehicle_type']
            occupancy = int(request.GET['occupancy'])
        except KeyError:
            return HttpResponse(
                content='Missing required parameters. Required parameters are: km(float), vehicle_type, occupancy(int)',
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            vehicle = Vehicle[vehicle_type]
        except KeyError:
            infos = {
                'note': 'Invalid vehicle type. Please choose from the following types',
                'types': [vehicle.name for vehicle in Vehicle],
            }

            return HttpResponse(
                content=json.dumps(infos),
                status=status.HTTP_400_BAD_REQUEST
            )

        co2_emission = Calculator.simple(distance, vehicle, occupancy)

        return JsonResponse({
            'CO2 emission (in g)': co2_emission,
            'Vehicle type': str(vehicle_type),
            'Distance (km)': distance,
            'Occupancy': occupancy,
            'Note': 'CO2 emissions are calculated in grams per kilometer. If occupancy is not provided, the emissions '
                    'are calculated for the maximum occupancy of the vehicle. If the occupancy exceeds the maximum '
                    'occupancy, an error will be thrown.',
        })
