from django.urls import path
from dashboard.views import DashboardView
from django.views.decorators.cache import never_cache

urlpatterns = [
    path(
        route='dashboard/',
        view=never_cache(DashboardView.as_view()),
        name="dashboard-page")
]