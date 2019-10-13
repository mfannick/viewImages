# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,Category,Editor
# import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
import pyperclip



# Create your views here.
def homePage(request):
    images = Image.getImages()
    yes='yes'
    return render(request,'homePage.html',{"images":images,'yes':yes})
# def homePage(request,anyDate):
#     date = dt.datetime.strptime(anyDate, '%Y-%m-%d').date()
#     images = Image.imageGetByDate(date)
#     return render(request,'homePage.html',{"date": date,"images":images})
# def homePage(request,category):
#     category=Category.get(id)
#     images = Image.imageGetByCategory(category=category)
#     return render(request,'homePage.html',{"category": category,"images":images})
def searchImageByCategory(request):
    if 'image' in request.GET and request.GET['image']:
        search_term=request.GET.get('image')
        images=Image.searchImageByCategory(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{'message':message,'images':images})
    else:
        message='no search yet'
        return render(request,'search.html',{'message':message})

# def searchImageByCategory(request):
#     if 'image' in request.GET and request.GET['image']:
#         search_term=request.GET.get('image')
#         images=Image.objects.filter(categoryF__categoryName__icontains=search_term)
#         message = f"{search_term}"

#         return render(request,'search.html',{'message':message,'images':images})
#     else:
#         message='no search yet'
#         return render(request,'search.html',{'message':message})

def imageDescription(request,imageId):
    try:
        imageIds=Image.objects.get(id=imageId)
    except ObjectDoesNotExist:
        raise Http404
    return render (request,'imageDescription.html',{'imageIds':imageIds})


  
