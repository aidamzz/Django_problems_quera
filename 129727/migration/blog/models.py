
from django.db import models
from pytz import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=True)


class Article(models.Model):
    l =(("d", "draft"), ("p", "publish"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    updated = models.DateTimeField(default=created)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(default='d', choices= l)



