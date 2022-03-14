from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from users.forms import PostForm, EditForm
from .models import Post
from django.urls import reverse_lazy, reverse


class Home(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'postDetails.html'

    def get_context_data(self, *args, **kwargs):
        
        amount = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = amount.total_likes()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)

        liked = False
        if amount.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'


class PostUpdate(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('site-home')


def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
