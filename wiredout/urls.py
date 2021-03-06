from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('register/', user_views.register, name='register'),
     path('', include('newsite.urls'), name='newsite_urls'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'),
          name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'
                                                   ), name='logout'),
     path('edit_profile/', user_views.EditProfile.as_view(),
          name='edit_profile'),
     path('password/', user_views.EditPassword.as_view
          (template_name='editPassword.html')),
     path('password_success/', user_views.PasswordSuccess,
          name='password_success'),
     path('<int:pk>/profile/', user_views.ProfilePage.as_view(),
          name='profile_page'),
     path('<int:pk>/edit_profile_page/', user_views.EditProfilePage.as_view(),
          name='edit_profile_page'),
     path('create_profile_page/', user_views.CreateProfilePage.as_view(),
          name='create_profile_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.
                          MEDIA_ROOT)
