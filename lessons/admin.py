from django.contrib import admin
from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "created_at", "updated_at")
    list_filter = ("course",)
    search_fields = ("title", "description")
