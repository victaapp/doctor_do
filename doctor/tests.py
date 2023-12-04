from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .response import *
from .models import *
import pdb

class UserTestCases(TestCase):
    def test_create_user(self):
        payload = {
            "username": "test",
            "email": "test@doc.com",
            "first_name": "test",
            "last_name": "test",
            "password": "Now@12345"
        }
        response = self.client.post(
            reverse("register_user"), data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], create_user['message'])


class DoctorTestCases(TestCase):
    def test_doctor_list(self):
        user_payload = {
            "username": "test",
            "email": "test@doc.com",
            "first_name": "test",
            "last_name": "test",
            "password": "Now@12345"
        }
        user_response = self.client.post(
            reverse("register_user"), data=user_payload, content_type="application/json")

        doctor_payload = {
            "user": user_response.data['user']['id'],
            "specialty": "Internal medicine",
            "education": "MBBS",
            "phone_number": 8627867890,
            "in_clinic_fee": 500,
            "video_fee": 350,
            "audio_fee": 350,
            "hospital": "",
            "address": "",
            "experience": 5
        }
        create_doc = self.client.post(
            reverse('doctors'), data=doctor_payload, content_type="application/json")

        response = self.client.get(reverse('doctors'))
        self.assertEqual(response.data[0].keys(), doctor_list[0].keys())
        self.assertEqual(response.status_code, 200)

    def test_doctor_create(self):
        user_payload = {
            "username": "test",
            "email": "test@doc.com",
            "first_name": "test",
            "last_name": "test",
            "password": "Now@12345"
        }
        user_response = self.client.post(
            reverse("register_user"), data=user_payload, content_type="application/json")

        payload = {
            "user": user_response.data['user']['id'],
            "specialty": "Internal medicine",
            "education": "MBBS",
            "phone_number": 8627867890,
            "in_clinic_fee": 500,
            "video_fee": 350,
            "audio_fee": 350,
            "hospital": "",
            "address": "",
            "experience": 5
        }
        response = self.client.post(
            reverse('doctors'), data=payload, content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_doctor_update(self):
        user_payload = {
            "username": "test",
            "email": "test@doc.com",
            "first_name": "test",
            "last_name": "test",
            "password": "Now@12345"
        }
        user_response = self.client.post(
            reverse("register_user"), data=user_payload, content_type="application/json")

        payload = {
            "user": user_response.data['user']['id'],
            "specialty": "Internal medicine",
            "education": "MBBS",
            "phone_number": 8627867890,
            "in_clinic_fee": 500,
            "video_fee": 350,
            "audio_fee": 350,
            "hospital": "",
            "address": "",
            "experience": 5
        }
        response = self.client.post(
            reverse('doctors'), data=payload, content_type="application/json")

        data_for_update = {
            "in_clinic_fee": 800,
            "video_fee": 500,
            "audio_fee": 500
        }
        doctor_id = response.data['id']
        response = self.client.patch(reverse('doctors_obj', args=[
                                     doctor_id]), data=data_for_update, content_type="application/json")
        self.assertEqual(response.status_code, 200)

        not_found_doctor_id = 23
        response = self.client.patch(reverse('doctors_obj', args=[
                                     not_found_doctor_id]), data=data_for_update, content_type="application/json")
        self.assertEqual(response.status_code, 404)



# Create your tests here.
class TreatmentsAPITest(TestCase):

    def test_create_treatment(self):
        payload = {
            "title": "Test treatment title",
            "description": "Test treatment description"
        }
        url = reverse('treatment')
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_get_treatments(self):
        payload = {
            "title": "Test treatment title",
            "description": "Test treatment description"
        }

        treatment_url = reverse('treatment')
        response_list = self.client.get(
            treatment_url, content_type="application/json")
        self.assertEqual(response_list.status_code, 200)
        
        
        Treatments.objects.create(title="title", description="description")
        treat_id = Treatments.objects.last().id
        treatment_url_obj = reverse('treatment_obj', args=[treat_id])
        pdb.set_trace()

        response_list_obj = self.client.get(treatment_url_obj, content_type="application/json")
        self.assertEqual(response_list_obj.status_code, 200)
