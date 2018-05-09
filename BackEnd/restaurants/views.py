from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views import View
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm, ItemForm
from .models import RestaurantLocation, Item
# Create your views here.


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


class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
        # slug = self.kwargs.get('slug')
        # if slug:
        #     queryset = RestaurantLocation.objects.all()
        # else:
        #     queryset = RestaurantLocation.objects.all()
        # return queryset


# class SearchRestaurantListView(ListView):
#     template_name = 'restaurants/restaurants_list.html'
#
#     def get_queryset(self):
#         queryset = RestaurantLocation.objects.filter(category__iexact='italian')
#         return queryset


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        queryset = RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = 'account/login'
    template_name = 'restaurants/form.html'
    # success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    login_url = 'account/login'
    template_name = 'form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Edit {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ItemForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Form'
        return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update View'
        return context


