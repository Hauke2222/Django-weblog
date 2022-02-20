from django.urls import path
from .views import index, log_detail, create_log, store_log, delete_log

urlpatterns = [
    path('', index, name='index'),
    path('create', create_log, name='create'),
    path('store', store_log, name='store'),
    path('post/<int:pk>/', log_detail, name='log_detail'),
    path('delete/<int:pk>/', delete_log, name='log_detail'),
]
