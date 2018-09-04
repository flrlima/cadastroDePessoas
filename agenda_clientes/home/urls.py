from django.urls import path
from .views import home, my_logout, HomePageView, MyView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('my_logout/', my_logout, name='my_logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html')), #ex para mostrar um html statico (genérica)
    path('home3/', HomePageView.as_view(template_name='home3.html')), #ex mesma coisa, ando override nos metodos
    path('view/', MyView.as_view()),


]