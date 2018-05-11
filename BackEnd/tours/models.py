from django.db import models
from accounts.models import UserAddresses
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
# Create your models here.


class TourQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class AvailableTourManger(models.Manager):
    def get_queryset(self):
        return TourQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()
        # queryset = super(AvailableTourManger, self).get_queryset().filter(available=True)
        # queryset = queryset  # TODO
        # return queryset


class Tour(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name=u'نام تور')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='Tour/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True, verbose_name=u'توضیحات تور')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'قیمت تور')
    available = models.BooleanField(default=True, verbose_name=u'موجود بودن')
    categories = models.ManyToManyField('Category', blank=True)
    default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
    start_tour = models.DateTimeField(blank=True, null=True)
    end_tour = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = AvailableTourManger()

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = u'تور'
        verbose_name_plural = u'تورها'

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('tours:Details_Tours', kwargs={"pk": self.pk,'slug':self.slug})


class TourVariation(models.Model):
    product = models.ForeignKey(Tour, on_delete=models.PROTECT)
    title = models.CharField(max_length=120, verbose_name=u'نام')
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default="-1", blank=True)  # unlimited

    def __str__(self):
        return self.title

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()


def tour_post_save_receiver(sender, instance, created, *args, **kwargs):
    print(sender)
    print(instance)
    print(created)


post_save.connect(tour_post_save_receiver, sender=Tour)


def image_upload_to(instance, filename):
    title = instance.tour.name
    slug = slugify(title)
    file_extension = filename.split(".")[1]
    new_filename = "{0}-{1}.{2}".format(slug, instance.id, file_extension)
    return "tours/{0}/{1}".format(slug, new_filename)


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.tour.name


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=False, blank=True, default='', verbose_name=u'توضیحات')
    active = models.BooleanField(default=True, verbose_name=u'فعال')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
