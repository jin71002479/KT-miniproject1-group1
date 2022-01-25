from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('<int:question_id>/', views.detail, name='detail'),
    path(
        'answer/create/<int:question_id>/', views.answer_create,
        name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    path('<int:question_id>/update/',views.update, name="update"),
    path('<int:question_id>/delete/',views.delete, name="delete"),
]
