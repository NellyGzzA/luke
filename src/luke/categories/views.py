from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'categories/index.html'

    @method_decorator(login_required(login_url='users:login'))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)
