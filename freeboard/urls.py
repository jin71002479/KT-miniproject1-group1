from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'freeboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('<int:freewrite_id>/', views.detail, name='detail'),
    path(
        'comment/create/<int:freewrite_id>/', views.comment_create,
        name='comment_create'),
    path('freewrite/create/', views.freewrite_create, name='freewrite_create'),
    path('freewrite/create2/', views.freewrite_create2, name='freewrite_create2'),
    path('<int:freewrite_id>/update/',views.update, name="update"),
    path('<int:freewrite_id>/delete/',views.delete, name="delete"),
    path('<int:comment_id>/comment_delete/',views.comment_delete, name="comment_delete"),
]