from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    blurb = models.CharField(mac_length=255, default='Click title to see full post')
    featured_image = CloudinaryField('image', default='placeholder')
    title_tag = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

# Order our posts by date posted
    class Meta:
        ordering = ['-date_posted']

# Returns string representation of the object
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.id])

