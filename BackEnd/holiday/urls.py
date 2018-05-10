"""holiday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
# <<<<<<< HEAD
from attractions.views import ContactView, AboutView, Index_Page
from django.conf import settings
from django.conf.urls.static import static
# =======
from django.contrib.auth.views import LoginView
# from restaurants.views import RestaurantCreateView, RestaurantListView
# >>>>>>> de58d38e14529a72a13b14df2c9787a8143c4ab4

urlpatterns = [
    url(r'^admin/', admin.site.urls),
# <<<<<<< HEAD
    url(r'^$', Index_Page, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
# =======
#     url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^login/$', LoginView.as_view(), name='login'),
# >>>>>>> de58d38e14529a72a13b14df2c9787a8143c4ab4
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    # url(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='restaurants-create'),
    # url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants-list'),
    # url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^accounts/', include('accounts.urls', namespace='account')),
    url(r'^tours/', include('tours.urls', namespace='tours')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)