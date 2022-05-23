from ssl import VERIFY_X509_TRUSTED_FIRST
from django.urls import path, include
from . import views


app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.RegisterView.as_view(), name='signup'),
]
