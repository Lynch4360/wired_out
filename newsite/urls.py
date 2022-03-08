from django.urls import path
from newsite import views as newsite_views

urlpatterns = [
    path('', newsite_views.Home.as_view(), name="site-home"),
    path('detail/<int:pk>', newsite_views.PostDetail.as_view(),
         name="post-detail"),
    path('add-post/', newsite_views.PostAdd.as_view(),
         name="post-add"),
    path('detail/edit/<int:pk>', newsite_views.PostUpdate.as_view(),
         name='post-update')
]
