from django.conf.urls import url
from .views import TourCategoryListView


urlpatterns = [
    url(r'^$', TourCategoryListView.as_view(), name='categories'),
]
