# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Editor,Image,Category,Location

# Register your models here.
admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
