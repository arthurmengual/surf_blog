from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    succes_url = reverse_lazy('accounts:login')
