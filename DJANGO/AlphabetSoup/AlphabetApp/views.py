from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class index(TemplateView):
    template_name = 'index.html'
    login_url = 'index.html'
    redirect_name = 'login_page'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, self.template_name, context = None)