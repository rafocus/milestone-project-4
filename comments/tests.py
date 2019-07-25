from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from main.models import Ticket
from .models import Comment

def test_display_all_comments(self):
        user = User.objects.create(username='testusername')
        ticket1 = Ticket.objects.create(title="test title 1", author=user)
        comment1 = Ticket.objects.create(content="comment 1", user=user, ticket=ticket1)
        comment2 = Ticket.objects.create(content="comment 2", user=user, ticket=ticket1)
        response = self.client.get(reverse('ticket-detail'))

        self.assertContains(response, comment1.content)
        self.assertContains(response, comment2.content)