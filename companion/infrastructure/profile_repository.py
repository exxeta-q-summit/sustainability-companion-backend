from django.db.models import QuerySet
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from companion.domain.profile import Profile


class ProfileRepository:
    @staticmethod
    @receiver(post_save, sender=Profile)
    def create(sender, instance, created, **kwargs) -> Profile | None:
        if created:
            return None

        return Profile.objects.create(
            username=instance.profile
        )

    @staticmethod
    @receiver(post_save, sender=Profile)
    def save(sender, instance, created, **kwargs) -> None:
        if not created:
            instance.save()

    @staticmethod
    @receiver(pre_delete, sender=Profile)
    def delete(sender, instance, **kwargs) -> None:
        pass

    @staticmethod
    def get_by_username(username) -> Profile:
        return Profile.objects.get(username=username)

    @staticmethod
    def get_all(order_by: str = None) -> QuerySet:
        # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by
        # order_by='-date'
        if order_by is not None:
            return Profile.objects.order_by(order_by)
        return Profile.objects.all()

    def get_count(self) -> int:
        return self.get_all().count()
