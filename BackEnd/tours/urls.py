from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^he$', views.TourListView.as_view(), name='Tour_List'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.TourDetailView,name='Tour_Detail'),
]
