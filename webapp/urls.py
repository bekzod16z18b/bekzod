"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('practical/', include('practical.urls')),
    path('articles1/', include('articles1.urls')),
    path('articles2/', include('articles2.urls')),
    path('articles3/', include('articles3.urls')),
    path('articles4/', include('articles4.urls')),
    path('articles5/', include('articles5.urls')),
    path('articles6/', include('articles6.urls')),
    path('articles7/', include('articles7.urls')),
    path('pycompiler/', include('pycompiler.urls')),
    path('', include('pages.urls')),
    path('Quiz/', include('Quiz.urls')),
    path('suzgame/', include('suzgame.urls')),
    path('songame/', include('songame.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)