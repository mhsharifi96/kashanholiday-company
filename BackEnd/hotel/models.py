from django.db import models
from attractions.models import Address
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'نام هتل', null=False, blank=True, default=u'امیرکبیر')
    introduction = models.TextField(null=False, blank=True, default='Welcome')
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def get_absolute_url(self):
        pass

    class Meta:
        pass


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
    # pass
    roomType = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    roomNumber = models.PositiveIntegerField(verbose_name=u'شماره اتاق', null=False, blank=False, default=100)

    def get_absolute_url(self):
        pass