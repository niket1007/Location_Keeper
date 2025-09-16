from django.views.generic.base import TemplateView
from location_keeper.utilities import ActiveUserLoggedInMixin
from dashboard.templates import TEMPLATES_PATH
from location_crud.models import Locations, Tags
from django.db.models import Q

class DashboardView(ActiveUserLoggedInMixin, TemplateView):
    template_name = TEMPLATES_PATH["DASHBOARD_PAGE"]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        userId = self.request.user.id
        context["full_name"] = self.request.user.first_name
        locations = Locations.objects.filter(user_id=userId).all()
        context["location_count"] = len(locations)
        context["tag_unique_count"] = Tags.objects.filter(user_id=userId).values('name').distinct().count()
        context["cities_unique_count"] = Locations.objects.filter(Q(user_id = userId) & ~Q(city = "") & ~Q(city = None)).values('city').distinct().count()
        context["locations_and_tags"] = []
        for location in locations:
            context["locations_and_tags"].append(
                {
                    "Location": location,
                    "Tags": Tags.objects.filter(location_id=location.id).all()
                })
        return context
