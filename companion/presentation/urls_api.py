from django.urls import path

from companion.presentation.homepage import HomepageApi

urlpatterns = [
    path('', HomepageApi.index)
]
