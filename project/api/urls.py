from django.urls import path

from .views.email_verification_view import VerifyEmail

urlpatterns = [
    path("auth/verify/<str:encoded_email>", VerifyEmail.as_view(), name="verify_email"),
]
