# Generated by Django 4.2.1 on 2024-04-20 20:23

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCert', models.CharField(max_length=100, verbose_name='Nome do Certificado')),
                ('dataCert', models.DateField(verbose_name='Data de Conclusão')),
                ('LinkCert', models.CharField(max_length=100, verbose_name='Link do Certificado')),
                ('duracaoCert', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Duração de Conclução do certificado')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='certificados', variations={'thumb': (124, 124)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('Numero', models.BigIntegerField(verbose_name='Numero')),
            ],
        ),
    ]
