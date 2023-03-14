
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Article_detail', args=[str(self.id)])


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'comments')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('articles_list')