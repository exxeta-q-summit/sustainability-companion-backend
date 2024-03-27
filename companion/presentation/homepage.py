from django.http import JsonResponse
from django.shortcuts import render

from companion.Application.profile_service import ProfileService
from companion.Application.trip_service import TripService
from companion.domain.serializers.profile_serializer import ProfileSerializer
from companion.domain.serializers.trip_serializer import TripSerializer


class HomepageView:
    user_service = ProfileService()
    trip_service = TripService()

    @classmethod
    def index(cls, request):
        all_users = cls.user_service.get_all_profiles()
        all_trips = cls.trip_service.get_all_trips()

        context = {
            'all_users': all_users,
            'all_trips': all_trips
        }

        return render(request, 'index.html', context)

    @classmethod
    def page_not_found(cls, request, pattern):
        context = {
            'broken': pattern
        }

        return render(request, '404.html', context)


class HomepageApi:
    user_service = ProfileService()
    trip_service = TripService()

    @classmethod
    def index(cls, request):
        all_users = cls.user_service.get_all_profiles()
        all_users = ProfileSerializer(all_users, many=True)

        all_trips = cls.trip_service.get_all_trips()
        all_trips = TripSerializer.serialize_all(all_trips)

        print(all_users)
        print(all_trips)

        context = {
            'all_users': all_users,
            'all_trips': all_trips
        }

        return JsonResponse(context)
