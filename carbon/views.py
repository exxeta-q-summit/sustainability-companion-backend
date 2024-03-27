import json

from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response

from carbon.carbon_calculator import Calculator
from carbon.vehicle_enum import Vehicle


class CarbonApi:

    @classmethod
    def simple(cls, request):
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
            'co2_emission': co2_emission,
            'vehicle_type': str(vehicle_type),
            'distance': distance,
            'occupancy': occupancy,
            'note': 'CO2 emissions are calculated in grams per kilometer. If occupancy is not provided, the emissions '
                    'are calculated for the maximum occupancy of the vehicle. If the occupancy exceeds the maximum '
                    'occupancy, an error will be thrown.',
        })

    @classmethod
    def complex(cls, request):
        # TODO: error handling
        distance = float(request.GET['km'])
        consumption_in_L_per_100km = float(request.GET['consumption_in_L_per_100km'])
        occupancy = int(request.GET['occupancy'] or 1)

        co2_emission = Calculator.complex(distance, consumption_in_L_per_100km, occupancy)

        return Response(data={
            'co2_emission': co2_emission,
            'distance': distance,
            'consumption_in_L_per_100km': consumption_in_L_per_100km,
            'occupancy': occupancy,
            'note': 'CO2 emissions are calculated in grams per kilometer. If occupancy is not provided, the emissions '
                    'are calculated for the maximum occupancy of the vehicle. If the occupancy exceeds the maximum '
                    'occupancy, an error will be thrown.',
        }, status=status.HTTP_200_OK)
