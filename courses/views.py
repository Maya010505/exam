from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course
from .forms import CourseForm
from .mixins import OwnerRequiredMixin
from django.db.models import Q


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = Course.objects.all()
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("courses:list")


class CourseUpdateView(OwnerRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

    def get_success_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(OwnerRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/course_confirm_delete.html"
    success_url = reverse_lazy("courses:list")
