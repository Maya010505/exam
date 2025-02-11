from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm
from .mixins import UserReviewMixin


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"
    paginate_by = 5

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        return Review.objects.filter(course_id=course_id)


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.object.course.id})


class ReviewUpdateView(UserReviewMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def get_success_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.object.course.id})


class ReviewDeleteView(UserReviewMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.object.course.id})
