from django.contrib import admin
from location_crud.models import Locations, Tags

class LocationAdminManger(admin.ModelAdmin):
    list_display = ['id', 'city', 'link', 'user_id']
    list_filter = ['city', 'user_id']
    search_fields = ['city']
    list_per_page = 50
admin.site.register(Locations, LocationAdminManger)

class TagAdminManger(admin.ModelAdmin):
    list_display = ['id', 'name', 'location_id', 'user_id']
    list_filter = ['name', 'location_id', 'user_id']
    search_fields = ['name']
    list_per_page=50
admin.site.register(Tags, TagAdminManger)