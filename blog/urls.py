from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('index/',views.index, name='index'),
    path('index2/',views.index2, name='index2'),
]
