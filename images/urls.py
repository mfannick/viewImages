from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$' ,views.homePage,name='homePage'),
    url(r'^search/', views.searchImageByCategory, name='searchImageByCategory'),
    url(r'^description/(\d+)',views.imageDescription,name='imageDescription')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)