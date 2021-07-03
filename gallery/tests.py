from django.test import TestCase
from .models import Category , Image , Location

# Create your tests here.
class CategoryTestClass(TestCase):
    #setup method
    def setUp(self):
        self.image = Category(selfies = 'Image')
        #test instances 
    def test_instance(self):
        self.assertTrue(isinstance(self.image , Category))

    # test save method
    def test_save_method(self):
        self.image.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) >0)

        



