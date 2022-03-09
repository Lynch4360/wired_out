from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    featured_image = CloudinaryField('image', default='placeholder')
    title_tag = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

# Order our posts by date posted
    class Meta:
        ordering = ['-date_posted']

# Returns string representation of the object
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))

# returns total number of likes on the post
    # def number_of_likes(self):
    #     return self.likes.count()


# STATUS = (
#     (0, "Draft"),
#     (1, "Published")
# )


# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=
# "posts")
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     featured_image = CloudinaryField('image', default='placeholder')
#     excerpt = models.TextField(blank=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     likes = models.ManyToManyField(User, related_name='post_likes', 
# blank=True)

# # Order our posts by created field
#     class Meta:
#         ordering = ['-created_on']

# # Returns string representation of the object
#     def __str__(self):
#         return self.title + ' | ' + str(self.author)


#     def get_absolute_url(self):
#         return reverse('site-home')
# returns total number of likes on the post
    # def number_of_likes(self):
    #     return self.likes.count()


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name=
# "comments")
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"
