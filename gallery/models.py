from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=46)

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

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    
    def update_location(self):
        self.update()

    def delete_location(self):
        self.delete()
    
class Gallery(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True, blank = True)
    name = models.CharField(max_length=46)
    descripton = models.TextField()
    location = models.ForeignKey('location',on_delete=models.CASCADE)
    category = models.ForeignKey('categories',on_delete=models.CASCADE)
    time_uploaded = models.DateTimeField(auto_now_add=True, null=True)   