from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class AvailableTourManger(models.Manager):
    def get_queryset(self):
        queryset = super(AvailableTourManger, self).get_queryset().filter(available=True)
        queryset = queryset  # TODO
        return queryset

class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=120, verbose_name=u'نام هتل', null=False, blank=True, default=u'امیرکبیر')
    slug = models.SlugField(null=False, blank=True, unique=True)
    image = models.ImageField(upload_to='Hotels/%Y/%m/%d', blank=True)
    description = models.TextField(null=False, blank=True, default='Welcome')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    available = models.BooleanField(default=True)

    objects = models.Manager()
    published = AvailableTourManger()


    def get_absolute_url(self):
        pass

    class Meta:
        ordering = ["-timestamp"]


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    typeName = models.CharField(max_length=120, verbose_name=u'نام نوع اتاق', null=False, blank=True)
    capacity = models.PositiveSmallIntegerField(verbose_name=u'ظرفیت اتاق', null=True, blank=True, default=2)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = u'نوع اتاق'
        verbose_name_plural = u'انواع اتاق'


class HotelRoom(models.Model):
    host = models.ForeignKey(User, on_delete=models.PROTECT)
    roomType = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    roomNumber = models.PositiveIntegerField(verbose_name=u'شماره اتاق', null=False, blank=False, default=100)

    def get_absolute_url(self):
        pass
