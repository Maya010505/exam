from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserUpdateForm


class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("courses:list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("courses:list")

class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/profile_update.html"
    success_url = reverse_lazy("users:profile")
