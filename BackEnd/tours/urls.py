from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Last_Tours, name='List_tour'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.Detals_Tours,name='Detals_Tours'),
]