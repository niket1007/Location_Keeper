from django.contrib.auth.mixins import UserPassesTestMixin

class ActiveUserLoggedInMixin(UserPassesTestMixin):
    def test_func(self):
        is_authenticated = self.request.user.is_authenticated
        is_active = self.request.user.is_active
        return is_authenticated and is_active
    
def isEmpty(value):
    return value == "" or value is None