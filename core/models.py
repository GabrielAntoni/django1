from django.db import models

# Create your models here.


class Visita(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    Numero = models.BigIntegerField('Numero')

    def __str__(self):
        return self.nome


class Certificado(models.Model):
    nomeCert = models.CharField('Nome do Certificado', max_length=100)
    dataCert = models.DateField('Data de Conclusão')
    LinkCert = models.CharField('Link do Certificado', max_length=100)
    duracaoCert = models.DecimalField('Duração de Conclução do certificado', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nomeCert

