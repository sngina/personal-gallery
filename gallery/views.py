from django.shortcuts import render ,redirect
from django.http import HttpResponse ,Http404
from . models import Image



# function that will be responsible for returning  images
def get_image(request):
    all_images = Image.objects.all()
    return render(request , 'photo/index.html' , {"all_images": all_images})

#function for searching images
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.image_search(search_term)
        message = f"{search_term}"

        return render(request, 'navbar.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render()
