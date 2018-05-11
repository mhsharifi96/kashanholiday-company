from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Created!")
    # if request.method == "POST":
    #     # print(request.POST)
    #
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Saved!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post-detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "object_list": queryset,
    #         "title": "Loged In"
    #     }
    # else:
    #     context = {
    #         "title": "Loged Out",
    #     }
    return render(request, "index-blog.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:list")
