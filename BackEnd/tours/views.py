from django.shortcuts import render

# Create your views here.
# class

from .models import Tour
import datetime


def Last_Tours(request):
    # query example =>blog.published.filter(title__startswith='Who')
    Today = datetime.date.today()
    Day_ago = Today -datetime.timedelta(days=2)
<<<<<<< HEAD
    last_tour = Tour.published.all()

    return render(request,'tours/list_tour.html',{'last_tour':last_tour})
=======
    query = Tour.published.filter(start_tour__range(Today, Day_ago))

    return render(request, 'tour/list_tour.html', {'last_tour': query})
>>>>>>> 903878bd6186d81e58ccc3aa0306330cc7917241

    
