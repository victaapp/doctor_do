from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from doctor.response import *
from doctor.models import *
import pdb
from .factories import FakeData

fk = FakeData()


def temporary_image():
    import tempfile
    from PIL import Image

    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(
        suffix='.jpg', prefix="test_img_")
    image.save(tmp_file, 'jpeg')
    tmp_file.seek(0)
    return tmp_file


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

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_doctor_list(self):
        doctor_payload = fk.doctor_data()
        doctor_payload['user'] = self.user.id
        doctor_payload['profile'] = temporary_image()

        create_doc = self.client.post(
            reverse('doctors'), data=doctor_payload, format='multipart')

        response = self.client.get(reverse('doctors'))
        self.assertEqual(response.data[0].keys(), doctor_list[0].keys())
        self.assertEqual(response.status_code, 200)

    def test_doctor_create(self):
        doctor_payload = fk.doctor_data()
        doctor_payload['user'] = self.user.id
        doctor_payload['profile'] = temporary_image()

        response = self.client.post(
            reverse('doctors'), data=doctor_payload, format='multipart')

        self.assertEqual(response.status_code, 201)

    def test_doctor_update(self):
        doctor_payload = fk.doctor_data()
        doctor_payload['user'] = self.user.id
        doctor_payload['profile'] = temporary_image()

        create_doc = self.client.post(
            reverse('doctors'), data=doctor_payload, format='multipart')

        data_for_update = {
            "in_clinic_fee": 800,
            "video_fee": 500,
            "audio_fee": 500
        }

        doctor_id = create_doc.data['id']
        response = self.client.patch(reverse('doctors_obj', args=[doctor_id]),
                                     data=data_for_update, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['in_clinic_fee'], 800)
        self.assertEqual(response.data['video_fee'], 500)
        self.assertEqual(response.data['audio_fee'], 500)
        not_found_doctor_id = 23
        response = self.client.patch(reverse('doctors_obj', args=[not_found_doctor_id]),
                                     data=data_for_update, content_type="application/json")
        self.assertEqual(response.status_code, 404)



class TreatmentsAPITest(TestCase):

    def test_create_treatment(self):
        payload = {
            "title": "Test treatment title",
            "description": "Test treatment description"
        }
        url = reverse('treatment')
        response = self.client.post(
            url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_get_treatments(self):
        treatment_url = reverse('treatment')
        response_list = self.client.get(
            treatment_url, content_type="application/json")
        self.assertEqual(response_list.status_code, 200)

        Treatments.objects.create(title="title", description="description")
        treat_id = Treatments.objects.last().id
        treatment_url_obj = reverse('treatment_obj', args=[treat_id])

        response_list_obj = self.client.get(
            treatment_url_obj, content_type="application/json")
        self.assertEqual(response_list_obj.status_code, 200)


from unittest.mock import patch, Mock
import logging

class TreatmentsAPITest(TestCase):

    @patch('doctor.logger.create_logger', new_callable=Mock)
    def test_create_treatment(self, mock_create_logger):
        # Disable logging during the test
        logging.disable(logging.CRITICAL)

        payload = {
            "title": "Test treatment title",
            "description": "Test treatment description"
        }
        url = reverse('treatment')

        with patch('doctor.logger.create_logger', new_callable=Mock):
            response = self.client.post(
                url, data=payload, content_type="application/json")

        mock_create_logger.assert_not_called()
        self.assertEqual(response.status_code, 201)

        # Re-enable logging after the test
        logging.disable(logging.NOTSET)

    @patch('doctor.logger.create_logger', new_callable=Mock)
    def test_create_treatment(self, mock_create_logger):
        payload = {
            "title": "Test treatment title",
            "description": "Test treatment description"
        }
        url = reverse('treatment')

        with patch('doctor.logger.create_logger', new_callable=Mock):
            response = self.client.post(
                url, data=payload, content_type="application/json")

        mock_create_logger.assert_not_called()
        self.assertEqual(response.status_code, 201)

    @patch('doctor.logger.create_logger', new_callable=Mock)
    def test_get_treatments(self, mock_create_logger):
        treatment_url = reverse('treatment')
        response_list = self.client.get(
            treatment_url, content_type="application/json")
        self.assertEqual(response_list.status_code, 200)

        Treatments.objects.create(title="title", description="description")
        treat_id = Treatments.objects.last().id
        treatment_url_obj = reverse('treatment_obj', args=[treat_id])

        with patch('doctor.logger.create_logger', new_callable=Mock):
            response_list_obj = self.client.get(
                treatment_url_obj, content_type="application/json")

        mock_create_logger.assert_not_called()
        self.assertEqual(response_list_obj.status_code, 200)
