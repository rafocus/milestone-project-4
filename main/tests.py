from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Ticket

class TestMainViews(TestCase):
    def setUp(self):
        User.objects.create(username="testuser")
        Ticket.objects.create(title="test title", author=User.objects.get(username='testuser'))
        Ticket.objects.create(title="test title 2", author=User.objects.get(username='testuser'))

    def test_main_list_view(self):
        response = self.client.get(reverse('main-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/ticket_list.html')

    def test_display_all_tickets(self):
        user = User.objects.get(username='testuser')
        ticket1 = Ticket.objects.get(title="test title", author=user)
        ticket2 = Ticket.objects.get(title="test title 2", author=user)
        response = self.client.get(reverse('main-home'))

        self.assertContains(response, ticket1.title)
        self.assertContains(response, ticket2.title)


    def test_main_detail_view(self):
        user = User.objects.get(username='testuser')
        ticket = Ticket.objects.get(title="test title", author=user)
        edit_url = reverse('ticket-detail', kwargs={'pk': ticket.id})
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)

class TestMainModels(TestCase):
    def setUp(self):
        User.objects.create(username="testuser")
        Ticket.objects.create(title="test title", author=User.objects.get(username='testuser'))

    def test_title(self):
        user = User.objects.get(username="testuser")
        ticket = Ticket.objects.get(author=user)
        self.assertEqual(ticket.title, "test title")