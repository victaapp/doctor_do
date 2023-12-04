from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving model instance first

        if self.profile:
            profile_img = Image.open(self.profile.path)

            # Resize the profile image
            profile_size = (600, 600)
            profile_img.thumbnail(profile_size)
            profile_img.save(self.profile.path)

            # Create a thumbnail
            thumb_size = (200, 200)
            thumb_img = profile_img.copy()
            thumb_img.thumbnail(thumb_size)

            # Save the thumbnail
            thumbnail_path = self.get_thumbnail_path()
            thumb_img.save(thumbnail_path)

            # Update the model instance with the thumbnail path
            self.thumbnail = thumbnail_path
            super().save(update_fields=['thumbnail'])

    def get_thumbnail_path(self):
        # Generate a unique filename for the thumbnail
        return f"doctor/profile/{self.user.username}_thumbnail.jpg"

class Treatments(models.Model):
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

class DoctorTreatments(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='doctor_treatments')
    treatment = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='treatments')

