from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
urlpatterns = [
    path('index/', views.index , name="index"),
    path('index2/', views.index2 , name="index2"),
    
]