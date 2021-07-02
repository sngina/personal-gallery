from django.db import models
from django.shortcuts import render , redirect
 # class
class Image(models.Model):
    image_name = models.CharField(max_length= 30)
    image_description = models.CharField(max_length=30)

    # the save function

    def save_image(self):
        self.save()
    # delete function for image
    def delete(self):
        self.delete()
   



