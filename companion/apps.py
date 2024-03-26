from django.apps import AppConfig


class CompanionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companion'

    def ready(self):
        print('Companion create signals...')

        from django.db.models.signals import post_save
        from django.db.models.signals import pre_delete
        from companion.domain.Profile import Profile
        from companion.domain.Trip import Trip
        from companion.infrastructure.profile_repository import ProfileRepository
        from companion.infrastructure.trip_repository import TripRepository

        post_save.connect(ProfileRepository.create, sender=Profile)
        post_save.connect(ProfileRepository.save, sender=Profile)
        pre_delete.connect(ProfileRepository.delete, sender=Profile)

        post_save.connect(TripRepository.create, sender=Trip)
        post_save.connect(TripRepository.save, sender=Trip)
        pre_delete.connect(TripRepository.delete, sender=Trip)
