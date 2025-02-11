from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course
from django.core.validators import MinValueValidator, MaxValueValidator
from exam.models import BaseModel

User = get_user_model()


class Review(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews', verbose_name="Курс")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Рейтинг")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.rating}/5)"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ('course', 'user')
