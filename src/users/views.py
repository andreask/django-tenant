from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

# Create your views here.


class LoginView(DjangoLoginView):
    ...


class LogoutView(DjangoLogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
