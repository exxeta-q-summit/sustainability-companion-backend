from django.urls import path

from carbon.views import CarbonApi

urlpatterns = [
    path('api/basic/', CarbonApi.basic),
]
