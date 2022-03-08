# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class Home(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'postDetails.html'


class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
    # fields = 'title', 'title_tag', 'author', 'content'
