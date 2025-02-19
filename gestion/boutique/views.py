from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from .models import Categorie,Produit,Commande,Facture,LigneCommande
from django.contrib import messages
from .forms import ProduitForm,CategorieForm,ClientForm
# Create your views here.
def index(request):
    categories = Categorie.objects.all()
    return render(request,'new_boutique/index.html',{'categories':categories})