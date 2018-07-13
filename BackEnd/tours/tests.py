from django.test import TestCase
from .models import Tour
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your tests here.

class TourModelTest(TestCase):

    #"""  models test"""
    def test_string_representation(self):
        tour= Tour(name="My Tour name",slug='this test slug',created=timezone.now())
        self.assertEqual(str(tour), tour.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Tour._meta.verbose_name_plural), "تورها") #tours


    #""" views and template test"""
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.user = get_user_model().objects.create(username='')
    
    #TODO:tours_tourvariation.sale_price
    # def test_one_Tour(self):
    #     Tour.objects.create(name='1-name', slug='1-slug', description='this is test ,its mean description' ,price=121.3)
    #     response = self.client.get('/')
    #     self.assertContains(response, '1-name')
    #     #self.assertContains(response, '1-slug')
    #     #self.assertContains(response, 'this is test ,its mean description')
    #     #self.assertContains(response, 121.3)
    




