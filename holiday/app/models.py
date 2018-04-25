from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
#class tours():

#class news():


class category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)

    class Meta:
        ordering =('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class AavailableTourManger(models.Manager):
    def get_queryset(self):
        queryset = super(AavailableTourManger, self).get_queryset().filter(available=True)
        queryset = queryset # TODO
        return queryset
    

class tour(models.Model):
    name = models.CharField(max_length=250,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    start_tour = models.DateTimeField(blank=True, null=True)
    end_tour = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects=models.Manager()
    published =AavailableTourManger()


    class Meta:
        ordering = ('-created',)
        index_together = (('id','slug'),)
        verbose_name = 'tour'
        verbose_name_plural='Tours'
    
    def __str__(self):
        return self.name


class PublishedBlogManger(models.Manager):
    def get_queryset(self):
        queryset = super(PublishedBlogManger, self).get_queryset().filter(status='published')
        queryset = queryset # TODO
        return queryset


class blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(category,related_name='category_blog')
    title = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True) 
    description = models.TextField(blank=True)
    #status = models.BooleanField(default=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedBlogManger()
    #query example =>blog.published.filter(title__startswith='Who')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural ='Blogs'


