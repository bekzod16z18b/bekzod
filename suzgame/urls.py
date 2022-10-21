from django.urls import path
from .views import homepagee, checkans

urlpatterns = [
    path('', homepagee, name = 'suzgame'),
    path('checkans', checkans, name = 'check'),
]

