from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import forms
from django.urls import reverse, reverse_lazy


# def home(request):
#     posts = models.Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'home.html', context=context)

class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'
    ordering = ['-date']


class DetailPostView(DetailView):
    model = models.Post
    template_name = 'post-detail.html'


# def add_post(request):
#     form = forms.PostForm()
#     if request.method == 'POST':
#         form = forms.PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home.html')
#     context = {'form': form}
#     return render(request, 'add-post', context=context)

class AddPost(CreateView):
    model = models.Post
    template_name = 'add-post.html'
    form_class = forms.PostForm


class UpdatePost(UpdateView):
    model = models.Post
    template_name = 'update-post.html'
    form_class = forms.UpdatePostForm


class DeletePost(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('blog:home')
