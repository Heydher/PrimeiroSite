import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateTimeField('Criação',  auto_now_add=True)
    modificado = models.DateTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-statis-up', 'Gráfico'),
        ('lni-users', 'Usuário'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-globe', 'web'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=13, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    ICONE_CHOISES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Computador'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Desing'),
        ('lni-mobile', 'celular'),
        ('lni-lock', 'cadeado'),
        ('lni-globe', 'web'),

    )
    POSICAO_CHOISES = (
        ('E', 'a esquerda'),
        ('D', 'a direita'),
    )
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOISES)
    posicao = models.CharField('Posição na página:', max_length=1, choices=POSICAO_CHOISES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo


class Preco(Base):
    ICONE_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )
    preco = models.BigIntegerField('Preço')
    nome = models.TextField('Nome', max_length=200)
    icone = models.CharField('Icone', max_length=11, choices=ICONE_CHOICES)
    descricao = models.TextField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return str(self.preco)

"""
class Fotos(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="media/images/fotos")
    texto = models.TextField()

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

        def __str__(self):
            return str(self.imagem)

"""