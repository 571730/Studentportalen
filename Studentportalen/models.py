from django.contrib.auth.models import Permission, User
from django.db import models
from .choices import *



class Emne(models.Model):
    navn = models.CharField(max_length=150)
    beskrivelse = models.CharField(max_length=300, default='Beskrivelse av faget')
    tags = models.CharField(max_length=100)
    vanskelig = models.FloatField(default=0)
    interesse = models.FloatField(default=0)
    arbeid = models.FloatField(default=0)
    info = models.TextField(max_length=1000)
    antall = models.IntegerField(default=0)

    def __str__(self):
        return self.navn


class Studie(models.Model):
    navn = models.CharField(max_length=100)
    rangering = models.FloatField()
    beskrivelse = models.TextField(max_length=1000)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.navn


class Vurdering(models.Model):
    emne = models.ForeignKey(Emne, default=1, on_delete=models.CASCADE)
    bruker = models.ForeignKey(User, default=1)
    tittel = models.CharField(default='Tittel', max_length=200)
    vanskelig = models.IntegerField(default=1, choices=VANSK_CHOICES)
    interesse = models.IntegerField(default=1, choices=INT_CHOICES)
    arbeid = models.IntegerField(default=1, choices=ARB_CHOICES)
    kommentar = models.TextField(max_length=2000)

    def __str__(self):
        return self.tittel
