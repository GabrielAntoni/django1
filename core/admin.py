from django.contrib import admin

# Register your models here.
from .models import Visita, Certificado


class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'Numero')


class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nomeCert', 'dataCert','duracaoCert')


admin.site.register(Visita, VisitaAdmin)
admin.site.register(Certificado, CertificadoAdmin)
