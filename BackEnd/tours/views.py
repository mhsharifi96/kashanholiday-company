from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.shortcuts import render
# Create your views here.
# class

from .models import Tour
from attractions.models import Gallery
import datetime


class TourDetailView(DetailView):
    model = Tour
    template_name = "tour_detail.html."


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


