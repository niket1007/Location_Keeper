from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from location_keeper.utilities import ActiveUserLoggedInMixin
from userprofile.forms import PasswordUpdateForm, NameUdpateForm
from django.contrib.auth import login, logout
from userprofile.templates import TEMPLATES_PATH

class ProfileView(ActiveUserLoggedInMixin, TemplateView):
    template_name = TEMPLATES_PATH["PROFILE_PAGE"]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.GET.get("update_name", None):
            result = self.request.GET["update_name"]
            context["update_name_result"] = result
         
        if self.request.GET.get("update_password", None):
            result = self.request.GET["update_password"]
            context["update_password_result"] = result
    
        context["update_password_form"] = PasswordUpdateForm()
        context["update_name_form"] = NameUdpateForm(
            data={
                "username": self.request.user.username,
                "full_name": self.request.user.first_name})
        return context
    
def update_name(request):
    if request.method == "POST":    
        form = NameUdpateForm(request.POST)
        query_msg = {"update_name": None}
        if form.is_valid():
            request.user.first_name = form.cleaned_data["full_name"]
            request.user.save()
            query_msg["update_name"] = "success"
        else:
            query_msg["update_name"] = "error"
        return redirect(reverse('profile-page', query=query_msg))

def update_password(request):
    if request.method == "POST":
        form = PasswordUpdateForm(request.POST)
        query_msg = {"update_password": None}
        if form.is_valid():
            new_password = form.cleaned_data["password"]
            request.user.set_password(new_password)
            request.user.save()
            login(request, request.user)
            query_msg["update_password"] = "success"
        else:
            query_msg["update_password"] = "error"
        return redirect(reverse('profile-page', query=query_msg))

def delete_account(request):
    if request.method == "POST":
        request.user.is_active = False
        request.user.save()
        logout(request=request)
        return redirect('login-page')