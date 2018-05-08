from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from .utils import unique_slug_generator
# Create your models here.

User = settings.AUTH_USER_MODEL


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'صاحب امتیاز', null=True)
    name = models.CharField(max_length=120, verbose_name=u'نام رستوران')
    location = models.CharField(max_length=120, null=True, blank=True, verbose_name=u'مکان')
    category = models.CharField(max_length=120, null=True, blank=True, validators=[], verbose_name=u'دسته بندی')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/restaurants/{self.slug}"
        return reverse('restaurant-detail', kwargs={'slug': self.slug})
    @property
    def title(self):
        return self.name

    class Meta:
        verbose_name = u'رستوران'
        verbose_name_plural = u'رستوران ها'


def restaurant_location_pre_save_receiver(sender, instance, *args, **kwargs): # before save
    print('Saving ...')
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def restaurant_location_post_save_receiver(sender, instance, created, *args, **kwargs): # after save
#     print('saved')
    # if not instance.slug:
    #     instance.slug = unique_slug_generator(instance)
    #     instance.save()


pre_save.connect(restaurant_location_pre_save_receiver, sender=RestaurantLocation)
# post_save.connect(restaurant_location_post_save_receiver, sender=RestaurantLocation)