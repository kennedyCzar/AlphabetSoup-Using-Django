from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.index.as_view(), name = 'index'),
]