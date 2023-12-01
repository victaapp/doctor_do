from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import DoctorAPI, RegisterApi, TreatmentsAPI

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterApi.as_view(), name='register_user'),

    path('/', DoctorAPI.as_view(), name="doctors"),
    path('<int:id>/', DoctorAPI.as_view(), name="doctors_obj"),

    path('treatment/', TreatmentsAPI.as_view(), name="treatment"),
    path('treatment/<int:id>/', TreatmentsAPI.as_view(), name="treatment_obj"),
]
