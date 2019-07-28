from django.shortcuts import render

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)