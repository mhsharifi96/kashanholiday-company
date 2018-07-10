from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
# class

from .models import Tour, TourVariation
from attractions.models import Gallery
import datetime
from django.utils import timezone


class TourVariationListView(ListView):
    model = Tour
    queryset = Tour.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TourVariationListView, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context
    # template_name = "tour_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(TourVariationListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        # if query:
        #     qs = self.model.objects.filter(
        #         Q(name__icontains=query) |
        #         Q(description__icontains=query)
        #     )
        return qs


class TourListView(ListView):
    model = Tour
    queryset = Tour.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TourListView, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context
    # template_name = "tour_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(TourListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


class TourDetailView(DetailView):
    model = Tour
    # template_name = "detail_tour.html"



# def product_detail_view_func(request, id):
#     tour_instance = Tour.objects.get(id=id)
#     template = "pagetour/tour_detail.html"
#     context = {
#         "object": tour_instance
#     }
#     return render(request, template, context)

def List_Tours(request):
    # query example =>blog.published.filter(title__startswith='Who')
    Today = datetime.date.today()
    # Day_ago = Today -datetime.timedelta(days=2)
    List_tour = Tour.published.order_by('?')[:6]
    Random_photo = Gallery.objects.order_by('?')[:6]
    return render(request,'tour/tour.html',{'List_tour':List_tour,'Random_photo':Random_photo})

    
def Details_Tours(request,id, slug):
    tour = get_object_or_404(Tour,id=id,slug=slug,available=True)
    #
    return render (request, 'tour/detail_tour.html',{'tour':tour})


