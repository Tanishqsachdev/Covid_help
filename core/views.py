from django.contrib.auth import forms, get_user_model
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserSignupForm

from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
# Create your views here.

class UserLogin(LoginView):
    redirect_authenticated_user=True
    template_name='core/login.html'
    def get_success_url(self) -> str:
        return reverse_lazy('home')

class Home(View):
    def get(self,*args, **kwargs):
        return render(self.request,'core/index.html')

class UserLogout(LogoutView):
    next_page='home'

class UserSignup(CreateView):
    template_name='core/register.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('user_login')

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        return reverse_lazy('user_signup')