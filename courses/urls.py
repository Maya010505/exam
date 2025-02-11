from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = "courses"

urlpatterns = [
    path('', CourseListView.as_view(), name="list"),
    path('<int:pk>/', CourseDetailView.as_view(), name="detail"),
    path('create/', CourseCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', CourseUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name="delete"),
]