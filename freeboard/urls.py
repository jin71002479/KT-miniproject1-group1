from django.urls import path, include
from . import views

app_name = 'freeboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:freewrite_id>/', views.detail, name='detail'),
    path(
        'comment/create/<int:freewrite_id>/', views.comment_create,
        name='comment_create'),
    path('freewrite/create/', views.freewrite_create, name='freewrite_create'),
    path('<int:freewrite_id>/update/',views.update, name="update"),
    path('<int:freewrite_id>/delete/',views.delete, name="delete"),
]