from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic.edit import FormView


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_next = 'categories:index'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_next)
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.success_next)


def logout_view(request):
    logout(request)
    return redirect('users:login')

login_view = LoginView.as_view()