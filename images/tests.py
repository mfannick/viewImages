# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Editor,Category,Image,Location
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.annick=Editor(userName='mfannick',email='mfannick1@gmail.com')
    #testing the instance
    def testInstance(self):
        self.assertTrue(isinstance(self.annick,Editor))
    
    # testing save function
    def testSaveInstance(self):
        self.annick.saveEditor()
        getInstance=Editor.objects.all()
        self.assertTrue(len(getInstance) >0 )

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.newLocation=Location(locationName='documents')
     #testing the instance
    def testInstance(self):
        self.assertTrue(isinstance(self.newLocation,Location))
    def testSaveLocationInstance(self):
        self.newLocation.saveLocation()
        getLocInstance=Location.objects.all()
        self.assertTrue(len(getLocInstance)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.newCategory=Category(categoryName='tech')
    def testCatInstance(self):
        self.assertTrue(isinstance(self.newCategory,Category))
    def testSaveCatInstance(self):
        self.newCategory.saveCategory()
        getCategory=Category.objects.all()
        self.assertTrue(len(getCategory)>0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.annick=Editor(userName='mfannick',email='mfannick1@gmail.com')
        self.annick.saveEditor()
        self.newLocation=Location(locationName='documents')
        self.newLocation.saveLocation()
        self.newCategory=Category(categoryName='tech')
        self.newCategory.saveCategory()

        # new Image
        self.newImage=Image(imageName='tech',imageDescription='tech',postedTime='2014-04-04',locationF=self.newLocation,editorF=self.annick,categoryF=self.newCategory)
        self.newImage.save()
    # def tearDown(self):
    #     Editor.objects.all().delete()
    #     Category.objects.all().delete()
    #     Location.objects.all().delete()
    #     Image.objects.all().delete()
        
        # testing the getting of the image
    def testGetImages(self):
        getImages=Image.getImages()
        self.assertTrue(len(getImages)>0)

    def testGetImageByDate(self):
        test_date = '2014-04-04'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        imagesByDate = Image.imageGetByDate(date)
        self.assertTrue(len(imagesByDate) == 0)
    # def testGetImageById(self):
    #     imagesById = Image.imageGetById()
    #     self.assertTrue(len(imagesById) == 0)

    def testDeleteImage(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.newImage.save()
        testImage=Image('mfannick1','kirikufifi@gmail.com') 
        testImage.save()

        self.newImage.deleteImage()# Deleting a image object
        self.assertEqual(len(testImage),1)

