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
})
def searchImageByCategory(request):
    if 'image' in request.GET and request.GET['image']:
        search_term=request.GET.get('image')
        images=Image.searchImageByCategory(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{'message':message,'images':images})
    else:
        message='no search yet'
        return render(request,'search.html',{'message':message})



def imageDescription(request,imageId):
    try:
        imageIds=Image.objects.get(id=imageId)
    except ObjectDoesNotExist:
        raise Http404
    return render (request,'imageDescription.html',{'imageIds':imageIds})


  
