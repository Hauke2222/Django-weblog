from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    context = get_list_or_404(Post.objects.all().order_by('-date'))
    return render(request, 'index.html', {'context': context})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    form = PostForm()
    return render(request, 'create_post.html', {'form': form, })


def store_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")


def update_post(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    post = get_object_or_404(Post, pk=pk)

    # pass the object as instance in form
    form = PostForm(request.POST or None, instance=post)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, 'update_post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponseRedirect("/")
