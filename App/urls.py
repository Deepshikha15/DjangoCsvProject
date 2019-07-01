
from django.contrib import admin
from django.urls import path,include
from csv_app.views import csv_upload
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('csv_upload', csv_upload, name="csv_upload")
    path('csv_app/', include('csv_app.urls')),
]
