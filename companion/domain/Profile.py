from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=255)

    ###
    # If you want to have a real user with authentication and so on,
    # combine the profile model with the user model, remove / refactor
    # the username and have them login via the user.
    ###

    # user = OneToOneField(User, on_delete=models.CASCADE)
    # default_transportation_type = models.CharField(
    #     choices=...
    # )

    def __str__(self):
        return f'{self.username}'
