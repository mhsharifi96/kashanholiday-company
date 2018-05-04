from django.db import models

# Create your models here.


class Address(models.Model):
    country = models.CharField(max_length=120, verbose_name=u'نام کشور', null=False, blank=False, default='Iran')
    state = models.CharField(max_length=120, verbose_name=u'نام استان', null=False, blank=False, default='Isfahan')
    city = models.CharField(max_length=120, verbose_name=u'نام شهر', null=False, blank=False, default='Kashan')
    address = models.TextField(null=False, blank=True, default='Amirkabir Ave')
    postalCode = models.CharField(max_length=10, null=False, blank=True, default='1234567890')
    # google_Map_API =
    class Meta:
        pass


class Attraction(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'نام مکان', null=False, blank=False, unique=True)
    introduction = models.TextField(null=False, blank=True, default=u'معرفی')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        pass

