from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Message
from django.contrib import messages

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Thank you {self.request.user.username} for contacting us, we will get back to you as soon as possible!')
        return super().form_valid(form)