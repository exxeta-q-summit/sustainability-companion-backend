from django.urls import path

from companion.presentation.api.profile_controller import ProfileApi
from companion.presentation.api.trip_controller import TripApi

urlpatterns = [
    path('profiles/', ProfileApi.as_view()),
    path('trips/', TripApi.as_view()),
]
