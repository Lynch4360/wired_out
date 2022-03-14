from django.contrib import admin
from .models import Post, UserProfile
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(UserProfile)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    summernote_field = ('content')

