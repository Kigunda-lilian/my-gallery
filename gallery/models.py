from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=46)

    def __str__(self):
            return self.name
        
class location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name