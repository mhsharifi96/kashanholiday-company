from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.


def home(request):
    pass


def about(request):
    pass


def contact(request):
    pass


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)
#
#     def post(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)
#
#     def put(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context

class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'