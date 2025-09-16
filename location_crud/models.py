from django.db import models
from django.contrib.auth.models import User

class Locations(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        help_text="User will provide location name")
    link = models.URLField(
        blank=False,
        null=False,
        help_text="User will provide the location link")
    city = models.CharField(
        blank=True,
        null=True,
        help_text="User will provide location city")
    user_id = models.ForeignKey(
        blank=False,
        null=False,
        to=User,
        on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+":"+self.name + ":" + self.city

class Tags(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        help_text="User will tag name for each location")
    location_id = models.ForeignKey(
        blank=False,
        null=False,
        to="Locations", 
        on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        blank=False,
        null=False,
        to=User,
        on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)+":"+self.name

