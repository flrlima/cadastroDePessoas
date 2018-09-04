from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


def calcular(valor1, valor2):
    return valor1 / valor2

# TODO: usar threads assim uepossivel
def home(request):
    numero1 = 10
    numero2 = 20
    resultado = calcular(numero1, numero2)
    return render(request, 'home/home.html', { 'resultado': resultado })

# FIXME: corrigir qlqr coisa
def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Passando valores home 3'
        return context

class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html') #Conteudo que devo passar para exibir

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')