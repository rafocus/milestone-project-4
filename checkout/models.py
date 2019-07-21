from django.db import models
from django.utils import timezone
from main.models import Ticket

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order('{self.id}', '{self.date}', '{self.full_name}')"


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.PROTECT)
    ticket = models.ForeignKey(Ticket, null=False, on_delete=models.PROTECT)
    payment = models.IntegerField(blank=False)

    def __str__(self):
        return f"OrderLineItem('{self.ticket.title}', '{self.payment}')"