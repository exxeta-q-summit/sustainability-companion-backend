from rest_framework import serializers

from companion.domain.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username"]
