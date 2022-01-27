"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from xml.etree.ElementInclude import include # 이진호가 추가함
from django.contrib import admin
from django.urls import path, include
from main import views
from userapp import views #이진호가 추가함
from django.conf.urls.static import static #이진호 추가 필수
from django.conf import settings #이진호 추가 필수
# from . import views as config_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('auth/', include('userapp.urls')),
    path('rank/', include('rank.urls')),
    path('quiz/', include('Quiz.urls')),
    path('blog/', include('blog.urls')),
    path('file/', include('file.urls')),
    path('board/', include('board.urls')),
    path('freeboard/', include('freeboard.urls')),
    path('paging/', include('paging.urls')),
    path('study/', include('study.urls')),
    path('youtubeboard/', include('youtubeboard.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
