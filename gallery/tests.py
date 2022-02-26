from django.test import TestCase
from .models import categories,location,Gallery

# Create your tests here.
class categoriesTestCase(TestCase):
    def setUp(self):
        self.fashion = categories(name = 'fashion')
