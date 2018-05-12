from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.


def post_create(request):
    # print("user" + request.user)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # if not request.author.is_authenticated():
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data.get("title"))
        instance.user = request.user
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


def listing(request):
    contact_list = 0


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post-detail.html", context)


def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active()  # .order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10)
    page_request_variable = "page"
    page = request.GET.get(page_request_variable)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "list",
        "page_request_var": page_request_variable,
        "today": today,
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


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:list")
