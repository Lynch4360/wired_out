from django.contrib import admin
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('newsite.urls'), name='newsite_urls'),
]
