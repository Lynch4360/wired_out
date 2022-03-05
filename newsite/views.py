from django.shortcuts import render
from django.http import HttpResponse
# from .models import Post, Post

def home(request):
    return HttpResponse('Home page')

def saved_posts(request):
    return HttpResponse('Saved Posts')

