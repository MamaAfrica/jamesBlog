from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    visible = (('Published', 'Published'), ('Drafted', 'Drafted'))
    title = models.CharField(max_length=20)
    Body = models.TextField()
    photo = models.ImageField(upload_to='uploaded_photos', null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=9, default='Drafted', choices=visible)
    slug = models.SlugField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #def get_absolute_url(self):
     #   return reverse(viewname="index", args=self.slug, kwargs=None,)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.title

class Trend(models.Model):
    visible = (('Published', 'Published'), ('Drafted', 'Drafted'))
    title = models.CharField(max_length=20)
    Body = models.TextField()
    photo = models.ImageField(upload_to='uploaded_photos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=9, default='Drafted', choices=visible)
    slug = models.SlugField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # def get_absolute_url(self):
    #   return reverse(viewname="index", args=self.slug, kwargs=None,)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.title

