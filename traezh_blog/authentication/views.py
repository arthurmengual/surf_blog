from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'registration/index.html')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login')
