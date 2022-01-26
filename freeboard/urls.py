from django.urls import path, include
from . import views

app_name = 'freeboard'

urlpatterns = [
    path('', views.index, name='index'),
]
