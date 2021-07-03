from django.shortcuts import render ,redirect
from django.http import HttpResponse ,Http404
from . models import Image



# function that will be responsible for returning  images
def get_image(request):
    all_images = Image.objects.all()
    return render(request , 'photo/index.html' , {"all_images": all_images})

