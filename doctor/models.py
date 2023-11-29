from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    experience = models.IntegerField()
    in_clinic_fee = models.IntegerField(null=True, blank=True)
    video_fee = models.IntegerField(null=True, blank=True)
    audio_fee = models.IntegerField(null=True, blank=True)
    profile = models.ImageField(upload_to='doctor/profile', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='doctor/profile', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} - {self.specialty} - {self.hospital}"


class Treatments(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='doctor_treatments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='treatments/icon', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='treatments/icon', null=True, blank=True)


class DoctorBlog(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='doctor_blog')
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/thumbnail', null=True, blank=True)





