from django.urls import path

from carbon.views import CarbonApi

urlpatterns = [
    path('api/simple/', CarbonApi.simple),
    path('api/complex/', CarbonApi.complex),
]
