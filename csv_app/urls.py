#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.csv_upload, name='csv_upload'),
    url(r'^searchposts/', views.searchposts, name='searchposts'),
    url(r'^IndexListing/', views.IndexListing, name='IndexListing'),
]