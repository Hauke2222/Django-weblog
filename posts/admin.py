from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Category
from .models import Comment


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
