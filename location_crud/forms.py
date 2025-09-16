from django import forms
from location_keeper.utilities import isEmpty

class LocationTagForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=15,
        label="Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "locationName",
                "title": "Enter location name",
                "placeholder": "e.g., Empire State Building"
            }))
    
    link = forms.URLField(
        label="Link",
        required=True,
        widget=forms.URLInput(
            attrs={
                "id": "locationLink",
                "title": "Enter link or click on generate link button",
                "placeholder": "Enter link or click on generate link button"
            }))
    
    city = forms.CharField(
        label="City",
        required=False,
        widget=forms.TextInput(
            attrs={
                "id": "locationCity",
                "title": "Enter location city",
                "placeholder": "Enter location city"
            }))
    
    tags = forms.CharField(
        label="Tags",
        required=False,
        widget=forms.TextInput(
            attrs={
                "onkeypress": "handleTagInput(event)",
                "id": "locationTags",
                "title": "Press Enter after each tag",
                "placeholder": "Press Enter after each tag"
            }))

    hidden_tags = forms.CharField(
        label="Hidden Tags",
        required=False,
        widget=forms.TextInput(
            attrs={
                "hidden": True,
                "id": "hiddenLocationTags"
            }))

    def clean_name(self):
        value = self.cleaned_data["name"]
        if isEmpty(value):
            raise forms.ValidationError("Location name should not be empty")
        return value
    
    def clean_link(self):
        value = self.cleaned_data["link"]
        if isEmpty(value):
            raise forms.ValidationError("Link should not be empty")
        return value
