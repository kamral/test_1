from django.db import models

# Create your models here.


class Books(models.Model):
    author=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    body=models.TextField()


    def __str__(self):
        return  self.title


