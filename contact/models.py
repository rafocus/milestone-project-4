from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title