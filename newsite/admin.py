from django.contrib import admin
from .models import Post, UserProfile, Comment
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(UserProfile)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    summernote_field = ('content')

