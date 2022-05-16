from pyexpat import model
from rest_framework import serializers
from db.models.user_model import User


class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'otp']
