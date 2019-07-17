from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Ticket(models.Model):
    PENDING = 'Pending'
    INPROGRESS = 'In progress'
    COMPLETED = 'Completed'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (INPROGRESS, 'In progress'),
        (COMPLETED, 'Completed')
    )

    BUG = 'Bug'
    FEATURE = 'Feature'
    ISSUE_CHOICES = (
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
    )

    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    ticket_type = models.CharField(max_length=100, choices=ISSUE_CHOICES, default=BUG)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=PENDING)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})