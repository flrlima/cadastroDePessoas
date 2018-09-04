from django.db import models

class Documento(models.Model):
    cpf_ou_cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.cpf_ou_cnpj

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)
    cpf_ou_cnpj = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        #return self.first_name + ' ' + self.last_name
        return  '{} {}'.format(self.first_name, self.last_name)


class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    numero = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descntos = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero