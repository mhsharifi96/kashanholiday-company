from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserAddresses(models.Model):
    country = models.CharField(max_length=120, verbose_name=u'کشور', default='Iran')
    state = models.CharField(max_length=120, verbose_name=u'استان', default='Isfahan')
    city = models.CharField(max_length=120, verbose_name=u'شهر', default='Kashan')
    postal_code = models.CharField(max_length=10, default=1234567890, verbose_name=u'کدپستی')


class BasicUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_address = models.ForeignKey(UserAddresses, on_delete=models.CASCADE)