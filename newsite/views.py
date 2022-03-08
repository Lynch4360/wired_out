from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class home(ListView):
    model = Post
    template_name = 'home.html'


class postDetail(DetailView):
    model = Post
    template_name = 'postDetails.html'

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
