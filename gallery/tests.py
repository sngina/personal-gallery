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
        #test delete method
    def test_delete_method(self):
        self.image.save_category()
        category = Category.objects.all()
        self.image.objects.filter(id = self.image.id).delete()
        self.assertTrue(len(category) ==0)
class ImageTestCase(TestCase):
    #creating new image and saving it.
    def setup(self):    
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >0)


