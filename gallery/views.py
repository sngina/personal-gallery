from django.shortcuts import render ,redirect
from django.http import HttpResponse ,Http404
from . models import Image



# function that will be responsible for returning  images
def get_image(request):
    all_images = Image.objects.all()
    return render(request , 'photo/index.html' , {"all_images": all_images})

#function for searching images
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'navbar.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render()
