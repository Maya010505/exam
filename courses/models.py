from django.db import models
from exam.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    start_date = models.DateField(verbose_name="Дата начала курса")
    end_date = models.DateField(verbose_name="Дата окончания курса")
    logo = models.ImageField(upload_to='course_logos/', null=True, blank=True, verbose_name="Логотип курса")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses", verbose_name="Автор курса")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

