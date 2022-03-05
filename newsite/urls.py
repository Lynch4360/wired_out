from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('saved_posts', views.saved_posts, name="saved_posts"),
]