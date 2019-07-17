from django.contrib.auth.models import User
from main.models import Ticket
from django.db import models

# Create your models here.
class Vote(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
        voted = models.BooleanField(default=False)

        def __str__(self):
            return f'{self.author}, {self.ticket}, {self.voted}'