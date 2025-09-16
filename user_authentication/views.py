from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from user_authentication.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from user_authentication.templates import TEMPLATES_PATH

class LoginView(TemplateView):
    template_name=TEMPLATES_PATH["LOGIN_PAGE"]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = LoginForm()
        return context_data
    
    def get(self, request):
        if request.user and request.user.is_authenticated:
            return redirect('dashboard-page')
        return super().get(request=request)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)

                if user:
                    login(request=request, user=user)
                    return redirect("dashboard-page")
                else:
                    form.add_error(None, 'Invalid credentials')
            else:
                form.add_error(None, 'Invalid credentials')
        return render(
            request=request, 
            template_name=self.template_name,
            context={"form": form})

class RegisterView(TemplateView):
    template_name=TEMPLATES_PATH["REGISTER_PAGE"]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = RegisterForm()
        return context_data

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['full_name']
            user = User(username=username, first_name=name)
            user.set_password(password)
            user.save()
            return redirect('login-page')
        return render(
            request=request, 
            template_name=self.template_name,
            context={"form": form})

def logout_view(request):
    logout(request=request)
    return redirect('login-page')