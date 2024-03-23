from typing import Any, Type
from django.contrib.auth.forms import AuthenticationForm
from django.forms.forms import BaseForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)

from users.models import User
from users.forms import (
    LoginForm, 
    RegisterForm, 
    UpdateMyProfileForm,
)


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    model = User
    success_url = reverse_lazy("home")

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        res = super().form_valid(form)
        login(self.request, form.instance)
        return res

class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "login.html"


class logoutView(DjangoLogoutView):
    pass


class MyProfileView(LoginRequiredMixin, FormView):
    form_class = UpdateMyProfileForm
    template_name = "my_profile.html"
    model = User

    def get_form(self, form_class: type | None = None) -> UpdateMyProfileForm:
        if form_class is None:
            form_class = self.get_form_class()
        user: User = self.request.user
        return form_class(instance=user)