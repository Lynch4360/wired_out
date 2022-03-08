from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    featured_image = CloudinaryField('image', default='placeholder')
    title_tag = models.CharField(max_length=255, default="WO | Article")
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

# Order our posts by date posted
    class Meta:
        ordering = ['-date_posted']

# Returns string representation of the object
    def __str__(self):
        return self.title

# returns total number of likes on the post
    def number_of_likes(self):
        return self.likes.count()
