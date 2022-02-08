from random import choices
from re import T
from django import forms
from django.conf import settings

from boutique.models import Magasin

# Formulaire de magasin
class MagasinForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type' : 'text',
                'class' : 'form-control'
            }
        )
    )
    country = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select',
                'class' : 'form-control'
            }
        )
    )
    created_at = forms.DateField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type' : 'date',
                'class' : 'form-control'
            }
        )
    )

# Formulaire de profil
class ProfilForm(forms.Form):
    email = forms.EmailField(
        max_length=200,
        required=True,
        min_length=2,
        widget=forms.EmailInput(
            attrs={
                'type' : 'email',
                'class' : 'form-control'
            }
        )
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'class' : 'form-control'
            }
        )
    )
    created_at = forms.DateField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type' : 'date',
                'class' : 'form-control'
                 
            }
        )
    )

# Formulaire de produit
class ProduitForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type' : 'text',
                'class' : 'form-control'
            }
        )
    )
    country = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select',
                'class' : 'form-control '
            }
        )
    )
    
    price = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type':'number',
                'class' : 'form-control '
            }
        )
    )
    
    image = forms.ImageField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'type':'upload',
                'class' : 'form-control '
            }
        )
    )
    
    created_at = forms.DateField(
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type' : 'date',
                'class' : 'form-control '
            }
        )
    )    