from django.contrib import admin
from .models import gallery,location,categories


#Register your models here.
# class galleryAdmin(admin.ModelAdmin):
#     prepopulated_field = {'gallery_slug':'(gallery_name)'}
#     # list_dispaly = ('gallery_name','gallery_slug','gallery_image')
    
# class locationAdmin(admin.ModelAdmin):
#     prepopulated_field = {'location_slug':'(location_name)'}
#     # list_dispaly = ('location_name','location_slug')
    
# class categoriesAdmin(admin.ModelAdmin):
#     prepopulated_field = {'categories_slug':'(categories_name)'}
#     # list_dispaly = ('categories_name','categories_slug') 
      
admin.site.register(gallery)
admin.site.register(location)
admin.site.register(categories)
