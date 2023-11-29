# from django.db import models
# from django.contrib.auth.models import AbstractUser

# TIME_CHOICES = [
#         ('00:00', '00:00'), ('00:30', '00:30'),
#         ('01:00', '01:00'), ('01:30', '01:30'),
#         ('02:00', '02:00'), ('02:30', '02:30'),
#         ('03:00', '03:00'), ('03:30', '03:30'),
#         ('04:00', '04:00'), ('04:30', '04:30'),
#         ('05:00', '05:00'), ('05:30', '05:30'),
#         ('06:00', '06:00'), ('06:30', '06:30'),
#         ('07:00', '07:00'), ('07:30', '07:30'),
#         ('08:00', '08:00'), ('08:30', '08:30'),
#         ('09:00', '09:00'), ('09:30', '09:30'),
#         ('10:00', '10:00'), ('10:30', '10:30'),
#         ('11:00', '11:00'), ('11:30', '11:30'),
#         ('12:00', '12:00'), ('12:30', '12:30'),
#         ('13:00', '13:00'), ('13:30', '13:30'),
#         ('14:00', '14:00'), ('14:30', '14:30'),
#         ('15:00', '15:00'), ('15:30', '15:30'),
#         ('16:00', '16:00'), ('16:30', '16:30'),
#         ('17:00', '17:00'), ('17:30', '17:30'),
#         ('18:00', '18:00'), ('18:30', '18:30'),
#         ('19:00', '19:00'), ('19:30', '19:30'),
#         ('20:00', '20:00'), ('20:30', '20:30'),
#         ('21:00', '21:00'), ('21:30', '21:30'),
#         ('22:00', '22:00'), ('22:30', '22:30'),
#         ('23:00', '23:00'), ('23:30', '23:30'),
#     ]

# GENDER_CHOICES = [
#         ("Male", 'Male'),
#         ("Female", 'Female'),
#         ("Other", 'Other'),
#     ]

# class CustomUser(AbstractUser):
#     profile_picture = models.ImageField(
#         upload_to='profile_pics/', null=True, blank=True)
#     is_doctor = models.BooleanField(default=False)
#     is_patient = models.BooleanField(default=False)
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=10)
#     age = models.IntegerField(null=True, blank=True)
#     gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
#     address = models.CharField(max_length=255, null=True, blank=True)
    
#     def save(self, *args, **kwargs):
#         if not self.name:
#             self.name = self.first_name + " " + self.last_name
#         super(CustomUser, self).save(*args, **kwargs)

# class Doctor(models.Model):
#     user = models.OneToOneField(
#         CustomUser, on_delete=models.CASCADE, primary_key=True)
#     specialty = models.CharField(max_length=255)
#     hospital = models.CharField(max_length=255)
#     availability_from = models.CharField(max_length=5, choices=TIME_CHOICES)
#     availability_to = models.CharField(max_length=5, choices=TIME_CHOICES)

#     def __str__(self):
#         return f"{self.user.username} - {self.specialty} - {self.hospital}"

# class Patient(models.Model):
#     user = models.OneToOneField(
#         CustomUser, on_delete=models.CASCADE, primary_key=True)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(
#         upload_to='patient/profile_pics/', null=True, blank=True)


# dctor_oppointment_status = (
#     ('Pending', 'Pending'),
#     ('Confirmed', 'Confirmed'),
#     ('Completed', 'Completed'),
#     ('Cancelled', 'Cancelled')
# )

# class DoctorsAppointment(models.Model):
#     doctor = models.ForeignKey(
#         Doctor, on_delete=models.CASCADE, related_name='doctor_appointments')
#     duration = models.IntegerField()
    
#     class Meta:
#         verbose_name = "Doctor Appointment"
#         verbose_name_plural = "Doctor Appointment"

#     def __str__(self):
#         return f"patient: {self.patient}, doctor: {self.doctor}, time: {self.date_time}"
