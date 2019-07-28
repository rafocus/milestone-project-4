from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Message(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('main-home')