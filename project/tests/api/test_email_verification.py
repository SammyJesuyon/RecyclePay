from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class TestEmailVerification(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.verify_email = reverse('verify_email')

    def test_verification_with_random_encoded_email(self):
        encoded_email = 'ZG1samRHOXlhV0ZyYVhScFoyOUFlV0ZvYjI4dVkyOXQ='
        res = self.client.get(self.verify_email+encoded_email)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

