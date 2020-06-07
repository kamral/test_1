from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments'
    )
    title=models.CharField(max_length=200)
    body=models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolutely_url(self):
        return reverse('article_list')