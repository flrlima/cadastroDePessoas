from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Produto
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import View

@login_required
def person_list(request):
    lista_de_pessoas = Person.objects.all()
    footer_message = "Mensagem passada do person_list"
    return render(request, 'person.html', { 'lista_de_pessoas' : lista_de_pessoas, 'footer_message': footer_message })

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', { 'form' : form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', { 'person': person })

class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    #success_url = '/clientes/person-list/'
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')

class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    #success_url = reverse_lazy('person_list_cbv')
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')

class PersonDelete(DeleteView):
    model = Person
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')

class ProdutoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maçã', 'Morango', 'Uva', 'Melancia']
        lista_de_produtos = []

        for produto in produtos:
            prod = Produto(descricao=produto, preco=10)
            lista_de_produtos.append(prod)

        Produto.objects.bulk_create(lista_de_produtos)

        return HttpResponse('Funcionou')