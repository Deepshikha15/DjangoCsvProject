
from django.contrib import admin
#from django.urls import path,include
from django.conf.urls import include,url
from csv_app.views import csv_upload

urlpatterns = [
    url(r'/', include('csv_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
