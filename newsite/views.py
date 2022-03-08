from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class home(ListView):
    model = Post
    template_name = 'home.html'


class postDetail(DetailView):
    model = Post
    template_name = 'postDetails.html'


class postAdd(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'


def about(request):
    return render(request, 'about.html', {'title': 'About'})
