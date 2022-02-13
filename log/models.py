from django.db import models

# Create your models here.


class Log(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title
