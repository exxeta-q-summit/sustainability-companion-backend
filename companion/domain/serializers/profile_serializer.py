from django.db.models import QuerySet

from companion.domain.Profile import Profile


class ProfileSerializer:
    @classmethod
    def serialize_all(cls, profiles: QuerySet):
        return [cls.serialize(profile) for profile in profiles]

    @classmethod
    def serialize(cls, profile: Profile):
        return {
            'username': profile.username,
        }
