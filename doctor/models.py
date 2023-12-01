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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Saving the main image first

        if self.profile:
            img = Image.open(self.profile.path)

            if img.height > 600 or img.width > 600:
                new_img = (600, 600)
                img.thumbnail(new_img)
                img.save(self.profile.path)

            # if img.height > 200 or img.width > 200:
            #     new_thmbimg = (200, 200)
            #     thmbimg = img.copy()  # Create a copy of the image for the thumbnail
            #     thmbimg.thumbnail(new_thmbimg)
            #     # Save the thumbnail with a different filename
            #     self.thumbnail.name = f"doctor/profile/{self.profile.name.split('/')[-1]}"
            #     thmbimg.save(self.thumbnail.path)

        super().save(*args, **kwargs)  # Save the model again to update the thumbnail field

    def __str__(self):
        return f"{self.user.username} - {self.specialty} - {self.hospital}"


class Treatments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='treatments/icon', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='treatments/icon', null=True, blank=True)

    def __str__(self):
        return self.title

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
        Treatments, on_delete=models.CASCADE, related_name='treatments')
    




