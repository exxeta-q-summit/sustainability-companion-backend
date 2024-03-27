from django.db.models import QuerySet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from companion.Application.profile_service import ProfileService
from companion.domain.profile import Profile
from companion.domain.serializers.profile_serializer import ProfileSerializer


class ProfileApi(APIView):
    profile_service = ProfileService()

    @classmethod
    def get(cls, request) -> Response:
        profiles = cls.profile_service.get_all_profiles()
        profiles = ProfileSerializer(profiles, many=True).data
        return Response(data=profiles, status=status.HTTP_200_OK)

    @classmethod
    def post(cls, request):
        try:
            username = request.data.get('username')
            if not username:
                raise ValueError('Username is required. Cannot be empty!')

            profile = Profile(username=username)
            cls.profile_service.save_profile(profile)
            profile = ProfileSerializer(profile).data

            return Response(data=profile, status=status.HTTP_201_CREATED)

        except AttributeError as _:
            return Response(data={
                'note': 'Username is already taken'
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(data={
                'note': 'Something when wrong! Make sure to include the following types',
                'params': {
                    'required': ['username']
                },
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def delete(cls, request):
        try:
            username = request.data.get('username')
            cls.profile_service.delete_by_username(username)
            return Response(status=status.HTTP_200_OK)
        except Profile.DoesNotExist as e:
            return Response(data={'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
