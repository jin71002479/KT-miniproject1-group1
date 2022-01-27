from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

# from .views import FileDownloadView

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('<int:question_id>/', views.detail, name='detail'),
    path(
        'answer/create/<int:question_id>/', views.answer_create,
        name='answer_create'),
    # path('question/create/', views.question_create, name='question_create'),

    path('<int:question_id>/update/',views.update, name="update"),
    path('<int:question_id>/delete/',views.delete, name="delete"),
    path('upload3/', views.upload3, name='upload3'),
    path('download/<int:question_id>/', views.download, name='download'),
    path('<int:answer_id>/comment_delete/',views.comment_delete, name="comment_delete"),
    # path('download/%3Fid=<int:question_id>/', views.download, name='download'),
    # path('download/', views.download, name='download'),
    # path('document/<int:document_id>/', FileDownloadView.as_view(), name="download"),
]
