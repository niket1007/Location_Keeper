from django.views.generic.base import TemplateView
from django.shortcuts import render,redirect
from location_keeper.utilities import ActiveUserLoggedInMixin
from location_crud.templates import TEMPLATES_PATH
from location_crud.forms import LocationTagForm
from location_crud.models import Locations, Tags
from location_crud.services import *
from django.shortcuts import get_object_or_404
#GMAP LINK = "https://www.google.com/maps/?q=<lat>,<lng>"

class AddLocationView(ActiveUserLoggedInMixin, TemplateView):
    template_name = TEMPLATES_PATH["ADD_LOCATION_PAGE"]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["page"] = {
            "title": "Add New Location",
            "subtitle": "Enter the location details manually"
        }
        context['form'] = LocationTagForm()
        context["errors"] = transform_error_payload(self.request.GET)
        return context
    
    def post(self, request):
        form = LocationTagForm(request.POST)
        if form.is_valid():
            show_success_message, show_error_message = create_location_and_tags(**form.cleaned_data, user=request.user)

        return render(
                request=request, 
                template_name=TEMPLATES_PATH["ADD_LOCATION_PAGE"],
                context={
                    "form": form,
                    "show_success_message": show_success_message,
                    "show_error_message": show_error_message})

class EditLocationView(ActiveUserLoggedInMixin, TemplateView):
    template_name = TEMPLATES_PATH["EDIT_LOCATION_PAGE"]
    location_data = None
    tags_data = None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["page"] = {
            "title": "Edit Location",
            "subtitle": "Edit the location details"
        }
        self.location_data = Locations.objects.get(id=kwargs['id'])
        self.tags_data = Tags.objects.filter(location_id=self.location_data.id)
        tags_string = transform_tag_data(self.tags_data)
        context['form'] = LocationTagForm(data={
            "name": self.location_data.name,
            "link": self.location_data.link,
            "city": self.location_data.city,
            "hidden_tags": tags_string
        })
        return context
    
    def post(self, request, id):
        form = LocationTagForm(request.POST)
        if form.is_valid():
            show_success_message, show_error_message = update_location_and_tags(
                user=request.user, location_id=id, **form.cleaned_data)
        return render(
                request=request, 
                template_name=TEMPLATES_PATH["EDIT_LOCATION_PAGE"],
                context={
                    "form": form,
                    "show_success_message": show_success_message,
                    "show_error_message": show_error_message})

def delete_location(request, id):
    location = get_object_or_404(Locations, pk=id)
    tags = Tags.objects.filter(location_id = location).all()
    for tag in tags:
        tag.delete()
    location.delete()
    return redirect('dashboard-page')