from django.shortcuts import render

# Create your views here.
# class

from .models import Tour
import datetime


def Last_Tours(request):
    # query example =>blog.published.filter(title__startswith='Who')
    Today = datetime.date.today()
    Day_ago = Today -datetime.timedelta(days=2)
    last_tour = Tour.published.all()

    return render(request,'tours/list_tour.html',{'last_tour':last_tour})

    
