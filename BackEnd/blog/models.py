from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=33, verbose_name=u'عنوان')
    image = models.ImageField(blank=True, null=True, verbose_name=u'تصویر تور')
    content = models.TextField(null=False, blank=True, default='', verbose_name=u'متن')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name=u'آخرین به روزرسانی')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=u'بارگذاری شده')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"id": self.id})
        # return "/posts/%s/" %(self.id)

    class Meta:
<<<<<<< HEAD
=======
        verbose_name = u'پست'
        verbose_name_plural = u'پست ها'
>>>>>>> 8f744b1d7dec51a8483f7c933e2273eb315e547d
        ordering = ["-timestamp", "-updated"]


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class PublishedBlogManger(models.Manager):
    def get_queryset(self):
        queryset = super(PublishedBlogManger, self).get_queryset().filter(status='published')
        queryset = queryset  # TODO
        return queryset


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, related_name='category_blog')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    # status = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedBlogManger()

    # query example =>blog.published.filter(title__startswith='Who')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural = 'Blogs'


