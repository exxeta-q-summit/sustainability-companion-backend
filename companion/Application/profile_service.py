from django.db.models import QuerySet

from companion.domain.profile import Profile
from companion.infrastructure.profile_repository import ProfileRepository


class ProfileService:
    profile_repository = ProfileRepository()

    def save_profile(self, profile: Profile):
        profile.save()

    def get_profile_by_username(self, username: str) -> Profile:
        profile = self.profile_repository.get_by_username(username=username)

        if profile is None:
            raise Exception('Profile not found')

        return profile

    def get_all_profiles(self, order_by: str = None) -> QuerySet:
        return self.profile_repository.get_all(order_by=order_by)
