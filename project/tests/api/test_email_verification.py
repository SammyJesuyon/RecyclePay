from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


verify_email = reverse('verify_email')

class TestEmailVerification(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_verification_with_random_otp(self):
        payload = {
            'email': 'test@mail.com',
            'otp': '54321'
        }
        res = self.client.post(verify_email, payload)
        self.assertEqual(res.status_code, 401)
        
    def test_verification_with_empty_fields(self):
        payload = {
            'email': '',
            'otp': ''
        }
        res = self.client.post(verify_email, payload)
        self.assertEqual(res.status_code, 401)