from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)

    sentiment = models.CharField(max_length=20)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def search(cls, query):
        return cls.objects.filter(title__icontains=query, published=True)