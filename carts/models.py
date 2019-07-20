from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from main.models import Ticket

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tickets     = models.ManyToManyField(Ticket, blank=True)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


