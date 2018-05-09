from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views



urlpatterns = [
    #url(r'^login/$','django.contrib.auth.views.login',name='login'),
    #url(r'^login/$', login , name='login'),
    #url(r'^logout/$', logout ,name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.register, name='signup'),

]
