from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "userapp"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('login2/', views.login2_view, name="login2"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup")
    
]
