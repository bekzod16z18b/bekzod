from django.urls import path
from .views import (
    indexdj,

)
urlpatterns = [
    path('', indexdj, name = 'index_dj'),

]
