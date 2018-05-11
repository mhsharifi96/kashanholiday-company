from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.List_Tours, name='List_Tour'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.Detals_Tours,name='Detals_Tours'),
]