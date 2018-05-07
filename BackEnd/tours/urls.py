from django.conf.urls import url
from . import views





urlpatterns = [
    url(r'^$',views.Last_Tours,name='Last_Tour'),
]