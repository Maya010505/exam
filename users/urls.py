from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileUpdateView, UserLogoutConfirmView

app_name = "users"


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    # Новый маршрут для страницы подтверждения выхода
    path('logout/confirm/', UserLogoutConfirmView.as_view(), name="logout_confirm"),
    # Маршрут для выполнения выхода (обрабатывает POST)
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('profile/', UserProfileUpdateView.as_view(), name="profile"),
]
