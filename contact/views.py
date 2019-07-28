from django.shortcuts import render
from django.views.generic import CreateView

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)