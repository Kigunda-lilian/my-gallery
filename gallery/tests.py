from django.test import TestCase
from .models import categories,location,Gallery

# Create your tests here.
class categoriesTestCase(TestCase):
    def setUp(self):
        self.fashion = categories(categories_name = 'fashion')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.fashion, categories))
        
        
    def test_save_method(self):
        self.fashion.save_category()
        category = categories.objects.all()
        self.assertTrue(categories)
        
    def test_delete_method(self):
        self.fashion.delete_category()
        category = categories.objects.all()
        self.assertTrue(categories)
        
    def test_update_method(self):
        self.fashion.update_category()
        category = categories.objects.all()
        self.assertTrue(categories)
        
class locationTestCase(TestCase):
    def setup(self):
        self.Kenya = location(location_name = 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya,location))
        
    def test_save_method(self):
        self.Kenya.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations)>0)
        
    def test_delete_method(self):
        self.Kenya.delete_location()
        locations = location.objects.all()
        self.assertTrue(len(locations)>0)
        
    def test_update_method(self):
        self.Kenya.update_location()
        locations = location.objects.all()
        self.assertTrue(len(locations)>0)


class GalleryTestCase(TestCase):
    def setUp(self):
        self.Nash = Image(Gallery_name = 'Nash', Gallery_description = 'Happy soul')
        self.Nash.save_image()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Nash, Image))
        
    def test_save_method(self):
        self.Nash.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_method(self):
        self.Nash.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_update_method(self):
        self.Nash.update_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)


