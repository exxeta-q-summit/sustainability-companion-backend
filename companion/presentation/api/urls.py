from django.urls import path

from companion.presentation.api.trip_controller import TripApi
from companion.presentation.homepage import HomepageApi

urlpatterns = [
    path('', HomepageApi.index),
    path('trips/', TripApi.as_view()),
]
