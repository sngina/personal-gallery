from django.shortcuts import render ,redirect
from django.http import HttpResponse ,Http404
from . models import Image


def welcome(request):
    return HttpResponse('Welcome to my  gallery')

