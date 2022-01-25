from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "study"

urlpatterns = [
    path('studying/', views.studying, name = "studying"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)