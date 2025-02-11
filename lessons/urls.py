from django.urls import path
from .views import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView

app_name = "lessons"

urlpatterns = [
    path('course/<int:course_id>/', LessonListView.as_view(), name="list"),
    path('<int:pk>/', LessonDetailView.as_view(), name="detail"),
    path('course/<int:course_id>/create/', LessonCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', LessonUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name="delete"),
]