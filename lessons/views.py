from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lesson
from .forms import LessonForm
from .mixins import OwnerRequiredMixin


class LessonListView(ListView):
    model = Lesson
    template_name = "lessons/lesson_list.html"
    context_object_name = "lessons"
    paginate_by = 10

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        queryset = Lesson.objects.all()
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset


class LessonDetailView(DetailView):
    model = Lesson
    template_name = "lessons/lesson_detail.html"


class LessonCreateView(OwnerRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "lessons/lesson_form.html"

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super().form_valid(form)

    def get_course(self):

        from courses.models import Course
        course_id = self.kwargs.get("course_id")
        return Course.objects.get(id=course_id)

    def get_success_url(self):
        return reverse_lazy("lessons:list", kwargs={"course_id": self.object.course.id})


class LessonUpdateView(OwnerRequiredMixin, UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = "lessons/lesson_form.html"

    def get_success_url(self):
        return reverse_lazy("lessons:detail", kwargs={"pk": self.object.pk})


class LessonDeleteView(OwnerRequiredMixin, DeleteView):
    model = Lesson
    template_name = "lessons/lesson_confirm_delete.html"
    success_url = reverse_lazy("courses:list")
