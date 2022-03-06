from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    summernote_field = ('content')

    
#     list_display = ('title', 'slug', 'status', 'date_posted')
#     prepopulated_field = {'slug': ('title',)}
#     list_filter = ('status', 'date_posted')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):

#     list_display = ('name', 'body', 'post', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)
