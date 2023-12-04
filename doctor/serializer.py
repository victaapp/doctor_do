from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', "email")
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class DoctorSerializer(serializers.ModelSerializer):
    user_ = UserSerializer(source="user", required=False)

    class Meta:
        model = Doctor
        fields = (
            "id",
            "user",
            "user_",
            "specialty",
            "hospital",
            "address",
            "education",
            "phone_number",
            "experience",
            "in_clinic_fee",
            "video_fee",
            "audio_fee",
            "profile",
            "thumbnail",
            "created_at",
            "updated_at"
        )


class TreatmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatments
        fields = "__all__"

class DoctorTreatmentsSerializer(serializers.ModelSerializer):
    treatment_ = TreatmentsSerializer(source="treatment", required=False)
    class Meta:
        model = DoctorTreatments
        fields = "__all__"
