from django.urls import path
from location_crud.views import AddLocationView, EditLocationView, delete_location
from django.views.decorators.cache import never_cache

urlpatterns = [
    path(
        route="locations/",
        view=never_cache(AddLocationView.as_view()),
        name="add-location-page"),
    path(
        route="locations/<int:id>",
        view=never_cache(EditLocationView.as_view()),
        name="edit-location-page"),
    path(
        route="delete/locations/<int:id>",
        view=never_cache(delete_location),
        name='delete-location-method')
]