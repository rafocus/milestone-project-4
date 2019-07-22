from django.db import models
from django.contrib.auth.models import User
from main.models import Ticket

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.user.username