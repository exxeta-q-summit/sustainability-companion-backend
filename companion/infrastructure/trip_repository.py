from django.db.models import QuerySet, Q
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from companion.domain.trip import Trip


class TripRepository:
    @staticmethod
    @receiver(post_save, sender=Trip)
    def create(sender, instance, created, **kwargs):
        if created:
            return None

        return Trip.objects.create(
            trip_id=instance.trip_id,
            profile=instance.profile,
            start=instance.start,
            destination=instance.destination,
            vehicle_type=instance.vehicle_type,
            co2_emissions=instance.co2_emissions
        )

    @staticmethod
    @receiver(post_save, sender=Trip)
    def save(sender, instance, created, **kwargs) -> None:
        if not created:
            instance.save()

    @staticmethod
    @receiver(pre_delete, sender=Trip)
    def delete(sender, instance, **kwargs) -> None:
        # If you want to perform some action before deleting the object
        # like deleting the associated files or something else
        # you can do it here
        pass

    @staticmethod
    def get_by_username(username) -> QuerySet:
        return Trip.objects.filter(profile=username)

    @staticmethod
    def get_by_filter(filter_dict) -> QuerySet:
        # VALIDATION OF FILTER_DICT IS CURRENTLY MISSING
        # ALSO THE QUERY IS FORCED ADD
        # https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query

        filter_query = Q(**filter_dict)
        return Trip.objects.filter(filter_query)

    @staticmethod
    def get_all(order_by: str = None) -> QuerySet:
        # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by
        # order_by='-date'
        if order_by:
            return Trip.objects.all().order_by(order_by)
        return Trip.objects.all()
