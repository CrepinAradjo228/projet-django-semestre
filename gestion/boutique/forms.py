from django import forms
from .models import Produit,Categorie,Client

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'quantite', 'categorie']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'email']
