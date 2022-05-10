from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('post-detail/<int:pk>', views.DetailPostView.as_view(), name='post-detail'),
    path('add-post', views.AddPost.as_view(), name='add-post'),
    path('update-post/<int:pk>', views.UpdatePost.as_view(), name='update-post'),
    path('delete-post/<int:pk>', views.DeletePost.as_view(), name='delete-post'),
]
