from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def all_photos(request):
   
    return render(request,'index.html')

def photo_description(request):
    
    return HttpResponse('This is my image description view')

def search_results(request):
   return HttpResponse('This is my where the searched categories will be displayed')

def profile(request):
       return HttpResponse('This is my profile page')

