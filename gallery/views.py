from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import gallery

# Create your views here.
def all_photos(request):
   
    images = gallery.objects.all()
    return render(request, 'index.html', {'images':images})


def photo_description(request,Gallery_image_id):
    
    image = gallery.objects.get(id=Gallery_image_id)
    return render(request, 'images.html', {'image':image})

def search_results(request):
    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_picture = gallery.search_by_category(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "images": searched_picture})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})

def profile(request):
       return HttpResponse('This is my profile page')

