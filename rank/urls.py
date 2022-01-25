from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "rank"

urlpatterns = [
    path('rank1_100/', views.rank1_100, name = "rank1_100"),
    path('insert/', views.insert),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)