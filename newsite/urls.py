from django.urls import path
from newsite import views as newsite_views

urlpatterns = [
    path('', newsite_views.home.as_view(), name="site-home"),
    path('detail/<int:pk>', newsite_views.postDetail.as_view(),
         name="post-detail"),
    path('add-post/', newsite_views.postAdd.as_view(),
         name="post-add"),
]