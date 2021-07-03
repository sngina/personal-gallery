from django.db import models
from django.shortcuts import render , redirect
 # class
class Category(models.Model):
    selfies = models.CharField(max_length= 50)
    # save function
    def save_category(self):
        self.save()
    #update function
    @classmethod
    def update_category(cls , id ,update):
        category = cls.objects.filter(id = id).update(selfies = update)
    #delete image
    def delete_category(self):
        self.delete()
class Location(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
        #save function
    def save_location(self):
        self.save()
        #update
    @classmethod
    def update_location(cls , id ,update):
        location = cls.objects.filter(id = id).update(name = update)
        #delete function
    def delete_location(self):
        self.delete()


class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'image/' , null = True)
    image_name = models.CharField(max_length= 30)
    image_description = models.CharField(max_length=30)
    image_category = models.ForeignKey(Category , null = True)
    image_location = models.ForeignKey(Location , null = True)
    # the save function

    def save_image(self):
        self.save()
    # delete function for image
    def delete(self):
        self.delete()
    @classmethod
    #update function
    def update(cls , id , update):
        name = cls.objects.filter(id = id ).update(image_photo = update)
        
    @classmethod
   #getting image by there id
    def get_image_by_id( cls ,id):
        get_image = cls.objects.filter()
       
       #search fuction
    @classmethod
    def search_image(cls , category):
        image = cls.objects.filter(image_category__selfies__icontains = category)
        return image
    @classmethod
    # function that filters image by location
    def filter_by_location( cls,location):
        location = cls.objects.filter(image_location__name__icontains = location)







   



