from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def all_photos(request):
   
    return HttpResponse('This is my where all my images will be displayed. also the homepage')

def photo_description(request, image_id):
    
    return HttpResponse('This is my image description view')

def search_results(request):
   return HttpResponse('This is my where the searched categories will be displayed')
