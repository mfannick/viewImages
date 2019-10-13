# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt
import pyperclip


# Create your models here.
class Editor(models.Model):
    userName=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self):
        return self.userName

    def saveEditor(self):
        self.save()

class Category(models.Model):
    categoryName=models.CharField(max_length=30)
    def __str__(self):
        return self.categoryName
    def saveCategory(self):
        self.save()
    
    

class Location(models.Model):
    locationName=models.CharField(max_length=30)
    def __str__(self):
        return self.locationName
    def saveLocation(self):
        self.save()

class Image(models.Model):
    image=models.ImageField(upload_to='imagesUpload/')
    imageName=models.CharField(max_length=30)
    imageDescription=models.TextField()
    imageUrl=models.URLField()
    postedTime=models.DateTimeField(auto_now_add=True)
    categoryF=models.ForeignKey(Category)
    locationF=models.ForeignKey(Location)
    editorF=models.ForeignKey(Editor)

    def __str__(self):
        return self.imageName

    @classmethod
    def getImages(cls):
        images=cls.objects.all()
        return images
    @classmethod
    def imageGetByDate(cls,date):
        imagesDate=cls.objects.filter(postedTime__date=date)
        return imagesDate
    
    @classmethod
    def imageGetById(cls):
        imageId=Image.objects.get(id)
        return imageId
    @classmethod
    def searchImageByCategory(cls,search_term):
        imageCategory = cls.objects.filter(categoryF__categoryName__icontains=search_term)
        return imageCategory
    @classmethod
    def delete_contact(cls):

        Image.remove()





