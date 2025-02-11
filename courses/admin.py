from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "start_date", "end_date", "created_at")
    list_filter = ("start_date", "end_date")
    search_fields = ("title", "description")