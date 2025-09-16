from django.urls import path
from user_authentication.views import LoginView, RegisterView, logout_view

urlpatterns = [
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