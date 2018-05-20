from django.db import models
from django.conf import settings
from django.db.models import Q
from .validators import validate_category
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from .utils import unique_slug_generator
from tours.models import Tour
# Create your models here.

User = settings.AUTH_USER_MODEL


class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self, query): #RestaurantLocation.objects.all().search(query) #RestaurantLocation.objects.filter(something).search()
        if query:
            query = query.strip()
            return self.filter(
                Q(name__icontains=query) |
                Q(location__icontains=query) |
                Q(location__iexact=query) |
                Q(category__icontains=query) |
                Q(category__iexact=query) |
                Q(item__name__icontains=query) |
                Q(item__contents__icontains=query)
                ).distinct()
        return self


class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'صاحب امتیاز')
    name = models.CharField(max_length=120, verbose_name=u'نام رستوران')
    location = models.CharField(max_length=120, null=True, blank=True, verbose_name=u'مکان')
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category], verbose_name=u'دسته بندی')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=True, default='')
    tour = models.ForeignKey(Tour, blank=True, null=True)

    def __str__(self):
        return self.name

    objects = RestaurantLocationManager()

    def get_absolute_url(self):
        # return f"/restaurants/{self.slug}"
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

    class Meta:
        verbose_name = u'رستوران'
        verbose_name_plural = u'رستوران ها'


def restaurant_location_pre_save_receiver(sender, instance, *args, **kwargs): # before save
    print('Saving ...')
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def restaurant_location_post_save_receiver(sender, instance, created, *args, **kwargs): # after save
#     print('saved')
    # if not instance.slug:
    #     instance.slug = unique_slug_generator(instance)
    #     instance.save()

pre_save.connect(restaurant_location_pre_save_receiver, sender=RestaurantLocation)
# post_save.connect(restaurant_location_post_save_receiver, sender=RestaurantLocation)


# class Item(models.Model):
#     user = models.ForeignKey(User)
#     restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.PROTECT)
#     name = models.CharField(max_length=120)
#     contents = models.TextField(help_text='separate each item by comma!')
#     excludes = models.TextField(blank=True, null=True, help_text='separate each item by comma!')
#     public = models.BooleanField(default=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['-updated', '-timestamp']
#
#     def get_contents(self):
#         return self.contents.split(",")
#
#     def get_excludes(self):
#         return self.excludes.split(",")
