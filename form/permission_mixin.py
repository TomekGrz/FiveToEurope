from django.contrib.auth.mixins import UserPassesTestMixin


class MyTestUserPassesTest(UserPassesTestMixin):

    def test_func(self):
        if self.request.user == self.get_object().owner:
            return True
        return False