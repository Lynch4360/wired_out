from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    # DeleteView
)


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


class PostUpdate(UpdateView):
    model = Post
    template_name = 'updatePost.html'
    fields = ['title', 'title_tag', 'content']
