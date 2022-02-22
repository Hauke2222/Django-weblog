from django.http import HttpResponse, HttpResponseRedirect
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


def update_log(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    log = get_object_or_404(Log, pk=pk)

    # pass the object as instance in form
    form = LogForm(request.POST or None, instance=log)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, 'update_log.html', context)


def delete_log(request, pk):
    log = Log.objects.get(pk=pk)
    log.delete()
    return HttpResponseRedirect("/")
