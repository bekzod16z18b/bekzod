from django.urls import path
from .views import (
    homea,
    addQuestion,
   # loginPage,
    logoutPage,
   # registerPage,

)

urlpatterns = [
    path('', homea, name='homea'),
    path('addQuestion/', addQuestion, name='addQuestion'),
   # path('login/', loginPage, name='login'),
    #path('logout/', logoutPage, name='logout'),
   # path('register/', registerPage, name='register'),
]
