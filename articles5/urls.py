from django.urls import path
from .views import (
    indexc,

)
urlpatterns = [
    path('', indexc, name = 'index_c'),

]
