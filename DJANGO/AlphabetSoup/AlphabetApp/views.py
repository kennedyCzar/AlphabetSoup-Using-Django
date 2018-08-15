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
            return render(request, self.template_name, context = None)


class alphabet(TemplateView):
    template_name = 'index.html'
    login_url = 'index.html'
    redirect_name = 'login_page'

    def post(self, request, **kwargs):
        if request.method == 'POST':
            self.message = request.POST.get('message')
            self.alphabets = request.POST.get('alphabets')
            asoup = AlphabetSoup(self.message, self.alphabets)
            asoup.Alphabet()
            return render(request, self.template_name, context = asoup.Alphabet())
    pass