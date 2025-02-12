from django.contrib.auth.mixins import UserPassesTestMixin


class UserReviewMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
