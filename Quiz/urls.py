from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('main2/', views.main2),
]