from django.urls import path
from .views.email_verification_view import VerifyEmail

urlpatterns = [
    path('api/v1/auth/verify/', VerifyEmail.as_view(), name='verify_email'),
]