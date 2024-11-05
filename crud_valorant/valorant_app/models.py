from django.db import models

# Create your models here.

class Mapa(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='mapas', null=True, blank=True)

class Personagem(models.Model):
    class Funcao(models.TextChoices):
        DUELISTA = 'DUELISTA', 'Duelista'
        INICIADOR = 'INICIADOR', 'Iniciador'
        CONTROLADOR = 'CONTROLADOR', 'Controlador'
        SENTINELA = 'SENTINELA', 'Sentinela'
        
    class Sexo(models.TextChoices):
        MASC = 'MASCULINO', 'Masculino'
        FEM = 'FEMININO', 'Feminino'
                
    nome = models.CharField(max_length = 155)
    habilidades = models.CharField(max_length = 255)
    funcao = models.CharField(max_length = 50, choices = Funcao.choices)
    sexo = models.CharField(max_length = 10, choices = Sexo.choices)
    origem = models.CharField(max_length = 255)
    imagem = models.ImageField(upload_to='personagens', null=True, blank=True)

class Arma(models.Model):
    class Tipo(models.TextChoices):
        PISTOLA = 'PISTOLA', 'Pistola'
        FUZIL = 'FUZIL', 'Fuzil'
        RIFLE = 'RIFLE', 'Rifle'
        SNIPER = 'SNIPER', 'Sniper'
        SUBMETRALHADORA = 'SUBMETRALHADORA', 'Submetralhadora'
        LMG = 'LMG', 'LMG'
        ESCOPETA = 'ESCOPETA', 'Escopeta'
        ARMA_BRANCA = 'ARMA_BRANCA', 'Arma Branca'
        
    nome = models.CharField(max_length = 255)
    tipo = models.CharField(max_length = 20, choices = Tipo.choices)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='armas', null=True, blank=True)

class Partida(models.Model):
    placar_time_1 = models.IntegerField()
    placar_time_2 = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField()
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    personagem = models.ManyToManyField(Personagem)