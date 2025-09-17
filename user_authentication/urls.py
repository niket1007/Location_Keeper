from django.urls import path
from user_authentication.views import LoginView, RegisterView, logout_view
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        route='',
        view=RedirectView.as_view(pattern_name="login-page"),
        name="home-page"),
    path(
        route='login/', 
        view=LoginView.as_view(), 
        name="login-page"),
    path(
        route='register/', 
        view=RegisterView.as_view(), 
        name="register-page"),
    path(
        route='logout/', 
        view=logout_view, 
        name="logout-page")
]