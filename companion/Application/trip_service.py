from uuid import UUID

from django.db.models import QuerySet

from companion.Application.profile_service import ProfileService
from companion.domain.trip import Trip
from companion.infrastructure.trip_repository import TripRepository


class TripService:
    trip_repository = TripRepository()
    profile_service = ProfileService()

    def save(self, trip: Trip):
        trip.save()

    def update(self, request) -> Trip:
        trip_queryset = self.get_by_id(request.data.get('id'))

        update_dict = {}

        try:
            profile = self.profile_service.get_profile_by_username(request.data.get('profile'))
            update_dict['profile'] = profile
        except Exception as e:
            pass

        for key, value in request.data.items():
            if key in ['start', 'destination', 'vehicle_type', 'co2_emissions']:
                update_dict[key] = value

        trip_queryset.update(**update_dict)

        return trip_queryset.first()

    def delete(self, id):
        self.get_by_id(id).delete()

    def get_trips_by_username(self, username: str) -> QuerySet:
        return self.trip_repository.get_by_username(username)

    def get_trips_by_filter(self, filter_dict) -> QuerySet:
        return self.trip_repository.get_by_filter(filter_dict)

    def get_all_trips(self) -> QuerySet:
        return self.trip_repository.get_all()

    def get_by_id(self, id) -> QuerySet:
        return self.trip_repository.get_by_filter({'id': id})
