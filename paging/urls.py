from django.urls import path
from . import views

app_name = 'paging'

urlpatterns = [
    path('question_list/', views.question_list, name='question_list'),
    path('api/', views.api, name='api'),
]