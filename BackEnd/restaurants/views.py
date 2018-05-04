from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views import View
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation
# Create your views here.


@login_required(login_url='/login/')
def restaurant_create_view(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    # if request.method == "POST":
    # form = RestaurantCreateForm(request.POST)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        # obj = RestaurantLocation.objects.create(
        #     name=form.cleaned_data.get('name'),
        #     location=form.cleaned_data.get('location'),
        #     category=form.cleaned_data.get('category'),
        # )
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        # print(form.errors)
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.all()
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


# class SearchRestaurantListView(ListView):
#     template_name = 'restaurants/restaurants_list.html'
#
#     def get_queryset(self):
#         queryset = RestaurantLocation.objects.filter(category__iexact='italian')
#         return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/form.html'
    success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)