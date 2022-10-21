from django.urls import path
from .views import homepagson, checkanson

urlpatterns = [
    path('', homepagson, name = 'songame'),
    path('checkanson', checkanson, name = 'checkson'),
]

