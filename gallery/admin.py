from django.contrib import admin
from .models import Gallery,location,categories


# Register your models here.
# class GalleryAdmin(admin.ModelAdmin):
#     prepopulated_field = {'Gallery_slug':'(Gallery_name)'}
#     list_dispaly = ('Gallery_name','Gallery_slug','Gallery_image')
    
# class locationAdmin(admin.ModelAdmin):
#     prepopulated_field = {'location_slug':'(location_name)'}
#     list_dispaly = ('location_name','location_slug')
    
# class categoriesAdmin(admin.ModelAdmin):
#     prepopulated_field = {'categories_slug':'(categories_name)'}
#     list_dispaly = ('categories_name','categories_slug') 
      
admin.site.register(Gallery)
admin.site.register(location)
admin.site.register(categories)
