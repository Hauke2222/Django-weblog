from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=250)
    text = models.TextField()
    note = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(
            field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields
        ]
