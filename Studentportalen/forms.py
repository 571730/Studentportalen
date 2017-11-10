from django import forms
from django.forms import ModelForm
from .models import Vurdering, User
from .choices import *
from django.utils.translation import ugettext_lazy as _


class VurderingForm(ModelForm):

    vanskelig = forms.ChoiceField(choices=VANSK_CHOICES, label='Hvor vanskelig er dette faget?'
                                  , widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), required=True)
    interesse = forms.ChoiceField(choices=INT_CHOICES, label='Hvor interessant er dette faget?'
                                  , widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ), required=True)
    arbeid = forms.ChoiceField(choices=ARB_CHOICES, label='Hvor mye arbeid krever dette faget?',
                               widget=forms.Select(
                                   attrs={
                                       'class': 'form-control'
                                   }
                               ), required=True)
    tittel = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Skriv en tittel..'
        }
    ), label='Skriv en tittel til din vurdering')

    kommentar = forms.CharField(label='Skriv din vurdering:', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Skriv din vurdering..'
        }
    ))

    class Meta:
        model = Vurdering
        fields = ['tittel', 'vanskelig', 'interesse', 'arbeid', 'kommentar']


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Velg et brukernavn:', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.CharField(label='Din epost:', widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = forms.CharField(label='Passord:', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password2 = forms.CharField(label='Gjenta passord:', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': _('Brukernavn'),
            'email': _('Epost'),
            'password': _('Passord'),
        }
class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Brukernavn', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    password = forms.CharField(label='Passord:', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))


    class Meta:
        model = User
        fields = ['username', 'password']
