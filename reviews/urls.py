from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = "reviews"

urlpatterns = [
    path('course/<int:course_id>/', ReviewListView.as_view(), name="list"),
    path('create/', ReviewCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name="delete"),
]