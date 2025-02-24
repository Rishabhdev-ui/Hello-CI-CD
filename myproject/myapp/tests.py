from django.test import TestCase
from django.urls import reverse

class SimpleTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, GitHub Actions!")
