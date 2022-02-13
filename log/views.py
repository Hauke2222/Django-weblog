from django.shortcuts import render, get_list_or_404
from .models import Log

# Create your views here.


def index(request):
    context = get_list_or_404(Log)
    return render(request, 'index.html', {'context': context})
