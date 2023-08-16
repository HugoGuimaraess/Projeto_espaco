from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Fotografia(models.Model):

    OPCAO = [
        ('NEBULOSA','nebulosa'),
        ('ESTRELA','Estrela'),
        ('GALAXIA','Galáxia'),
        ('PLANETA','Planeta')
    ]

    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda= models.CharField(max_length=150,null=False,blank=False)
    descricao = models.TextField(null=False,blank=False)
    foto = models.ImageField(upload_to='Fotos/%Y/%m/%d/',blank=True)
    publicada = models.BooleanField(default=False)
    categoria = models.CharField(choices=OPCAO,max_length=100,default='')
    data = models.DateTimeField(default=datetime.now,blank=False)
    tipo = models.CharField(choices=OPCAO,default='',max_length=100)
    usuario = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True,blank=False,related_name='user')


    def __str__(self):
        return self.nome
