from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Log
from .forms import LogForm

# Create your views here.


def index(request):
    context = get_list_or_404(Log)
    return render(request, 'index.html', {'context': context})


def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'log_detail.html', {'log': log})


def create_log(request):
    form = LogForm()
    return render(request, 'create_log.html', {'form': form, })


def store_log(request):
    form = LogForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('Your log post has been saved')


def delete_log(request, pk):
    log = Log.objects.get(pk=pk)
    log.delete()
    return HttpResponse('Your log post has been deleted')
