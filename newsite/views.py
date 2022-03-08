from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

class home(ListView):
    model = Post
    template_name = 'home.html'


class postDetail(DetailView):
    model = Post
    template_name = 'postDetails.html'


class postAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
    # fields = 'title', 'title_tag', 'author', 'content'

