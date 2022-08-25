# Generated by Django 4.0.6 on 2022-08-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_recurso_icone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('preco', models.BigIntegerField(max_length=100, verbose_name='Preço')),
                ('nome', models.TextField(max_length=200, verbose_name='Nome')),
                ('icone', models.CharField(choices=[('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=13, verbose_name='Icone')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Preço',
                'verbose_name_plural': 'Preços',
            },
        ),
    ]