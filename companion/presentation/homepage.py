from django.http import JsonResponse
from django.shortcuts import render

from companion.Application.profile_service import ProfileService
from companion.domain.serializers.profile_serializer import ProfileSerializer


class HomepageView:
    user_service = ProfileService()

    @classmethod
    def index(cls, request):
        all_users = cls.user_service.get_all_profiles()

        context = {
            'all_users': all_users
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

    @classmethod
    def index(cls, request):
        all_users = cls.user_service.get_all_profiles()
        all_users = ProfileSerializer.serialize_all(all_users)

        context = {
            'all_users': all_users
        }

        return JsonResponse(context)
