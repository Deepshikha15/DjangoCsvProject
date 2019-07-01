from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.csv_upload, name='csv_upload'),
    path('searchposts/', views.searchposts, name='searchposts'),
    path('IndexListing/', views.IndexListing, name='IndexListing'),
]