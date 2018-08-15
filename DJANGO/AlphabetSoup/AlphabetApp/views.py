from django.shortcuts import render
from django.views.generic import TemplateView
from . import AlphabetSoup
# Create your views here.


class index(TemplateView):
    template_name = 'index.html'
    login_url = 'index.html'
    redirect_name = 'login_page'
    def get(self, request, **kwargs):
        if request.method == 'GET':
            self.message = request.GET.get('message')
            self.alphabets = request.GET.get('alphabets')
            asoup = AlphabetSoup.AlphabetSoup(self.message, self.alphabets)
            output = asoup.Alphabet()
            return render(request, self.template_name, {'output': output})
