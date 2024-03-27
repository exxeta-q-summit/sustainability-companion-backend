from rest_framework import serializers

from companion.domain.trip import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id',
            'profile',
            'start',
            'destination',
            'vehicle_type',
            'co2_emissions',
        ]
