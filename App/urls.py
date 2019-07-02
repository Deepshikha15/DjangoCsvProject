
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include,url
from csv_app.views import csv_upload

urlpatterns = [
    path('csv_app/', include('csv_app.urls')),
    path('admin/', admin.site.urls),
]
