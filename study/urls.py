from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
app_name = "study"

urlpatterns = [
    path('studying/', views.studying, name = "studying"),
    path('studying2/', views.studying2, name = "studying2"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)