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


def ajout_produit(request):
    categories = Categorie.objects.all()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():  # Vérifie si le formulaire est valide
            nom = form.cleaned_data['nom']
            prix = form.cleaned_data['prix']
            quantite = form.cleaned_data['quantite']
            categorie = form.cleaned_data['categorie']
            produit = Produit(nom=nom, prix=prix, quantite=quantite, categorie=categorie)
            produit.save()
            messages.success(request, "Produit créé avec succès.")
            return redirect('gestion_produit')  # Redirige vers la page de gestion des produits

    # Si la méthode n'est pas POST ou si le formulaire est invalide
    form = ProduitForm()  # Crée un nouveau formulaire
    return render(request, 'new_boutique/ajout_produit.html', {'form': form, 'categories': categories})

def gestion_produit(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'new_boutique/gestion_produit.html', {'produits': produits,'categories':categories})



    
def ajout_categorie(request):
    categories = Categorie.objects.all()
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            categorie = Categorie(nom=nom)
            categorie.save()
            return redirect ('gestion_produit')
        
    else:
        form = ProduitForm()  # Crée un nouveau formulaire
        return render(request, 'new_boutique/ajout_categorie.html', {'form': form, 'categories': categories})
    
def supprimer_produit(request, id):
    if request.method == 'GET':
        Produit.objects.get(id=id).delete()
        return redirect('gestion_produit')
    else:
        return redirect('gestion_produit')

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('gestion_produit')  # Redirige vers la page de gestion des produits
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'new_boutique/modifier_produit.html', {'form': form, 'produit': produit})



def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    # Récupérer le panier depuis la session
    panier = request.session.get('panier', {})

    # Ajouter le produit au panier ou mettre à jour la quantité
    if str(produit_id) in panier:
        panier[str(produit_id)] += 1
    else:
        panier[str(produit_id)] = 1

    # Enregistrer le panier dans la session
    request.session['panier'] = panier

    return redirect('gestion_produit')



def voir_panier(request):
    panier = request.session.get('panier', {})
    produits = []
    total = 0

    for produit_id, quantite in panier.items():
        produit = Produit.objects.get(id=produit_id)
        total_ligne = produit.prix * quantite
        produits.append({
            'produit': produit,
            'quantite': quantite,
            'total_ligne': total_ligne,
        })
        total += total_ligne

    return render(request, 'new_boutique/panier.html', {'produits': produits, 'total': total})

def valider_commande(request):
    panier = request.session.get('panier', {})
    if not panier:
        return redirect('gestion_produit')

    if request.method == 'POST':
        # Traiter le formulaire soumis
        form = ClientForm(request.POST)
        if form.is_valid():
            # Créer un nouveau client avec les données du formulaire
            client = form.save()

            # Créer une nouvelle commande
            commande = Commande.objects.create(client=client, complete=True)

            # Ajouter les produits du panier à la commande
            for produit_id, quantite in panier.items():
                produit = Produit.objects.get(id=produit_id)
                LigneCommande.objects.create(
                    commande=commande,
                    produit=produit,
                    quantite=quantite,
                    prix_unitaire=produit.prix,  # Utiliser le prix unitaire du produit
                )

            # Calculer le total de la commande à partir des lignes de commande
            total = sum(ligne.prix_unitaire * ligne.quantite for ligne in commande.lignecommande_set.all())

            # Créer la facture
            facture = Facture.objects.create(commande=commande, total=total)

            # Vider le panier
            request.session['panier'] = {}

            return redirect('detail_facture', facture_id=facture.id)
    else:
        # Afficher le formulaire vide
        form = ClientForm()

    return render(request, 'new_boutique/valider_commande.html', {'form': form})




def gestion_commandes(request):
    categories = Categorie.objects.all()
    # Récupérer toutes les commandes
    commandes = Commande.objects.all().order_by('-date_commande')  # Tri par date décroissante
    return render(request, 'new_boutique/gestion_commande.html', {'commandes': commandes,'categories':categories})





def detail_commande(request, commande_id):
    # Récupérer la commande par son ID
    commande = get_object_or_404(Commande, id=commande_id)
    return render(request, 'new_boutique/detail_commande.html', {'commande': commande})







def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    return render(request, 'new_boutique/detail_facture.html', {'facture': facture})













def supprimer_du_panier(request, produit_id):
    # Récupérer le panier depuis la session
    panier = request.session.get('panier', {})

    # Vérifier si le produit est dans le panier
    if str(produit_id) in panier:
        # Supprimer le produit du panier
        del panier[str(produit_id)]
        # Mettre à jour la session
        request.session['panier'] = panier

    # Rediriger vers la page du panier
    return redirect('voir_panier')



def gestion_facture(request):
    categories = Categorie.objects.all()
    # Récupérer toutes les factures
    factures = Facture.objects.all().order_by('-date_facture')  # Tri par date décroissante
    return render(request, 'new_boutique/gestion_facture.html', {'factures': factures,'categories':categories})




def tableau_de_bord(request):
    # Statistiques des ventes par mois
    ventes_par_mois = Facture.objects.annotate(
        mois=TruncMonth('date_facture')
    ).values('mois').annotate(
        total_ventes=Sum('total')
    ).order_by('mois')

    # Produits les plus vendus
    produits_plus_vendus = Produit.objects.annotate(
        total_vendu=Sum('lignecommande__quantite')
    ).order_by('-total_vendu')[:5]

    # Commandes par statut
    commandes_par_statut = Commande.objects.values(
        'complete'
    ).annotate(
        total=Count('id')
    )

    # Préparer les données pour les graphiques
    mois = [vente['mois'].strftime('%Y-%m') for vente in ventes_par_mois]
    ventes = [float(vente['total_ventes']) for vente in ventes_par_mois]

    produits = [produit.nom for produit in produits_plus_vendus]
    quantites = [produit.total_vendu for produit in produits_plus_vendus]

    statuts = ["Terminée" if statut['complete'] else "En cours" for statut in commandes_par_statut]
    total_commandes = [statut['total'] for statut in commandes_par_statut]
    categories = Categorie.objects.all()

    return render(request, 'new_boutique/tableau_de_bord.html', {
        'mois': mois,
        'ventes': ventes,
        'produits': produits,
        'quantites': quantites,
        'statuts': statuts,
        'total_commandes': total_commandes,
        'categories':categories
    })

