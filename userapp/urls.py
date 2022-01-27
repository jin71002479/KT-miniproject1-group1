from urllib.parse import urlparse
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "userapp"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('login2/', views.login2_view, name="login2"),
    path('logout/', views.logout_view, name="logout"),
    path('logout2/', views.logout2_view, name="logout2"),
    path('signup/', views.signup_view, name="signup"),
    path('signup2/', views.signup2_view, name="signup2"),
    
]
