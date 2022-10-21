from django.urls import path
from .views import (
    indexp,

)
urlpatterns = [
    path('', indexp, name = 'index_p'),

]
