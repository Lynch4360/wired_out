from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from users.forms import PostForm, EditForm
from .models import Post


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
    form_class = EditForm
    template_name = 'updatePost.html'


class PostDelete(DeleteView):
    model = PostFormtemplatE_name = 'deletePost.html'
