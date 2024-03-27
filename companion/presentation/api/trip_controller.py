import json

from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from companion.Application.profile_service import ProfileService
from companion.Application.trip_service import TripService
from companion.domain.serializers.trip_serializer import TripSerializer
from companion.domain.trip import Trip


class TripApi(APIView):
    trip_service = TripService()
    profile_service = ProfileService()

    @classmethod
    def get(cls, request):
        # if there are query parameters, we can use them to return more complex data
        # validate(**kwargs) # allowed parameters only

        trips = cls.trip_service.get_trips_by_filter(request.GET.dict())
        trips = TripSerializer(trips, many=True).data

        return Response(data=trips, status=status.HTTP_200_OK)

    @classmethod
    def post(cls, request):
        ####
        ## IDEA FOR FUTURE IMPLEMENTATION
        ## ONLY ALLOW POST REQUESTS FROM AUTHENTICATED USERS
        ####
        # if not request.user.is_authenticated:
        #     return JsonResponse({
        #         'code': 401,
        #         'message': 'Unauthorized'
        #     })
        try:
            profile = cls.profile_service.get_profile_by_username(request.data.get('profile'))
            trip = Trip(
                profile=profile,
                start=request.data.get('start'),
                destination=request.data.get('destination'),
                vehicle_type=request.data.get('vehicle_type'),
                co2_emissions=request.data.get('co2_emissions'),
            )
            cls.trip_service.save(trip)
            trip = TripSerializer(trip).data
            return Response(data=trip, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({
                'code': 500,
                'note': 'Something when wrong! Make sure to include the following types',
                'params': {
                    'required': ["username", "start", "destination", "vehicle_type"],
                    'optional': ["co2_emissions"]
                },
                'message': str(e)
            })

    @classmethod
    def put(cls, request):
        ####
        ## IDEA FOR FUTURE IMPLEMENTATION
        ## ONLY ALLOW POST REQUESTS FROM AUTHENTICATED USERS
        ####
        # if not request.user.is_authenticated:
        #     return JsonResponse({
        #         'code': 401,
        #         'message': 'Unauthorized'
        #     })
        try:
            trip = cls.trip_service.update(request)
            trip = TripSerializer(trip).data
            return Response(data=trip, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({
                'code': 500,
                'note': 'Something when wrong! Make sure to include the following types',
                'params': {
                    'required': ["id"],
                    'optional': ["username", "start", "destination", "vehicle_type", "co2_emissions"]
                },
                'message': str(e)
            })

    @classmethod
    def delete(cls, request):
        # if not request.user.is_authenticated:
        #     return JsonResponse({
        #         'code': 401,
        #         'message': 'Unauthorized'
        #     })

        try:
            trip_id = request.data.get('id')
            cls.trip_service.delete(trip_id)
            return Response(status=status.HTTP_200_OK)
        except Trip.DoesNotExist as e:
            return Response(data={'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
