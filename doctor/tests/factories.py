import factory
from django.contrib.auth.models import User
from doctor.models import Doctor
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')

class DoctorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Doctor

    user = factory.SubFactory(UserFactory)
    specialty = fake.random_element(elements=('Cardiologist', 'Dermatologist', 'Orthopedic', 'Pediatrician'))
    hospital = fake.company()
    address = fake.address()
    education = fake.word()
    phone_number = fake.random_int(min=1000000000, max=9999999999, step=1)
    experience = fake.random_int(min=0, max=30)
    in_clinic_fee = fake.random_int(min=50, max=500, step=10)
    video_fee = fake.random_int(min=20, max=200, step=10)
    audio_fee = fake.random_int(min=10, max=100, step=10)
    profile = factory.django.ImageField(filename='profile.jpg', color='green')
    thumbnail = factory.django.ImageField(filename='thumbnail.jpg', color='blue')


class FakeData():
    def doctor_data(self):
        data = {
            "specialty" : fake.random_element(elements=('Cardiologist', 'Dermatologist', 'Orthopedic', 'Pediatrician')),
            "hospital" : fake.company(),
            "address" : fake.address(),
            "education" : fake.word(),
            "phone_number" : fake.random_int(min=1000000000, max=9999999999, step=1),
            "experience" : fake.random_int(min=0, max=30),
            "in_clinic_fee" : fake.random_int(min=50, max=500, step=10),
            "video_fee" : fake.random_int(min=20, max=200, step=10),
            "audio_fee" : fake.random_int(min=10, max=100, step=10),
        }

        return data
