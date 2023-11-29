# # yourapp/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import *


# @receiver(post_save, sender=Doctor)
# def doctor_created(sender, instance, created, **kwargs):
#     if created:
#         # Perform actions when a new user is created
#         print(f"User {instance.username} created!")
