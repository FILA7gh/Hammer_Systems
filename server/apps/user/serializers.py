from rest_framework import serializers

from .models import CustomUser, InvitationCode


class InviteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationCode
        fields = ['code']


class UserInvitedNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number']


class UserProfileSerializer(serializers.ModelSerializer):
    activated_by = UserInvitedNumbersSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'activated_code', 'is_activated', 'activated_by']
