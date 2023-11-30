from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import DoctorListAPI, RegisterApi

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterApi.as_view(), name='register_user'),

    path('', DoctorListAPI.as_view(), name="doctors"),
    path('<int:id>', DoctorListAPI.as_view(), name="doctors_obj"),
]
