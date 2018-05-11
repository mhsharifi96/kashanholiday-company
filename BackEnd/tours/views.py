from django.shortcuts import render,get_object_or_404

# Create your views here.
# class

from .models import Tour
from attractions.models import Gallery
import datetime


def List_Tours(request):
    # query example =>blog.published.filter(title__startswith='Who')
    Today = datetime.date.today()
    # Day_ago = Today -datetime.timedelta(days=2)
    List_tour = Tour.published.order_by('?')[:6]
    Random_photo = Gallery.objects.order_by('?')[:6]
    return render(request,'tour/tour.html',{'List_tour':List_tour,'Random_photo':Random_photo})

    
def Detals_Tours(request, id, slug):
    tour = get_object_or_404(Tour,id=id,slug=slug,available=True)
    return render (request, 'tours/tour_detail.html',{'tour':tour})


