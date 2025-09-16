from django.urls import path
from userprofile.views import ProfileView, update_name, update_password, delete_account
from django.views.decorators.cache import never_cache

urlpatterns = [
    path(
        route="profile/",
        view=never_cache(ProfileView.as_view()),
        name="profile-page"),
    path(
        route="update/user",
        view=never_cache(update_name),
        name="update-user-method"),
    path(
        route="update/password",
        view=never_cache(update_password),
        name="update-password-method"),
    path(
        route="delete/account",
        view=never_cache(delete_account),
        name="delete-account-method"
    )
]