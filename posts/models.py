from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields
        ]


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
