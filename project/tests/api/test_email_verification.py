from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from db.models import User
from lib.utils import Util


class TestEmailVerification(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.verify_email = reverse('verify_email')
        self.email = 'dummy@yahoo.com'
        self.password = '123456'
        User.
        
    def test_verification_with_random_otp(self):
        payload = 'dmljdG9yaWFraXRpZ29AeWFob28uY29t'

        res = self.client.get(self.verify_email+payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    # def test_verification_with_empty_fields(self):
    #     payload = {
    #         'email': '',
    #
    #     }
    #     res = self.client.post(self.verify_email, payload)
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
