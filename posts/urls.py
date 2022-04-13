from django.urls import path
from .views import (
    index,
    post_detail,
    create_post,
    store_post,
    update_post,
    delete_post,
    store_comment,
)

urlpatterns = [
    path("", index, name="index"),
    path("create", create_post, name="create"),
    path("store", store_post, name="store"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("update/<int:pk>/", update_post, name="update_post"),
    path("delete/<int:pk>/", delete_post, name="delete_post"),
    path("store_comment", store_comment, name="store_comment"),
]
