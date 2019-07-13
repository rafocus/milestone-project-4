from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('main-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'Issuetrack')

class TestPage(TestCase):
    def test_about_page_works(self):
        response = self.client.get(reverse('main-about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertContains(response, 'Issuetrack')