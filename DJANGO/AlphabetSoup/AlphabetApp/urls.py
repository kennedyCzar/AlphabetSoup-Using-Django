from django.conf.urls import url
from . import views

#urls pattarns as created in views

urlpatterns = [
    url('^$', views.index.as_view(), name = 'index'),
    url('^$', views.alphabet.as_view(), name = 'alphabet'),
]
