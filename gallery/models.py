
from unicodedata import category
from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=46)
    # categories_slug=models.SlugField(max_length=50)
    
    # class meta:
    #         verbose_name = "category"
    #         verbose_name_plural = "categories"

    def __str__(self):
            return self.name
        
    def save_category(self):
        self.save()

    def update_category(self):
        self.update()

    def delete_category(self):
        self.delete()    
        
class location(models.Model):
    name = models.CharField(max_length=46)
    # location_slug=models.SlugField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    
    def update_location(self):
        self.update()

    def delete_location(self):
        self.delete()
    
class gallery(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True, blank = True)
    name = models.CharField(max_length=46)
    descripton = models.TextField(max_length=500)
    # gallery_slug=models.SlugField(max_length=50)
    location = models.ForeignKey(location,on_delete=models.CASCADE)
    category = models.ForeignKey(categories,on_delete=models.CASCADE)
    time_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    
    # class meta:
    #         verbose_name = "Gallery"
    #         verbose_name_plural = "Galleries"

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__name__icontains=search_term)

        return gallery
    def __str__(self):
        return self.name
    
    
    def save_image(self):
            self.save()
    
    def update_image(self):
        self.save()

    def delete_image(self):
        self.delete()   