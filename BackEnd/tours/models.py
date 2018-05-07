from django.db import models
from accounts.models import UserAddresses
from django.urls import reverse
# Create your models here.


class AvailableTourManger(models.Manager):
    def get_queryset(self):
        queryset = super(AvailableTourManger, self).get_queryset().filter(available=True)
        queryset = queryset  # TODO
        return queryset


class Tour(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    start_tour = models.DateTimeField(blank=True, null=True)
    end_tour = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = AvailableTourManger()

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = 'tour'
        verbose_name_plural = 'Tours'

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('last_tour:tour_detail', args=[self.slug,self.id])


