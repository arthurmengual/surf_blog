from argparse import Namespace
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('authentication.urls', namespace='authentication')),
    path('', include('blog.urls', namespace='blog')),
]
