from django import template

register = template.Library()
'''
@register.filter
def meu_filtro(data):
    return "{} - Teste do filtro".format(data)
'''

@register.filter
def meu_filtro(valor):
    return "{} - Teste do filtro".format(valor)

@register.filter
def arredondamento_de_casas(valor, casa_decimal):
    return round(valor, casa_decimal)